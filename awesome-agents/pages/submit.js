import { useState } from 'react';

const questions = [
  { field: 'title', question: 'What is the title of your agent or app?' },
  { field: 'description', question: 'Please provide a brief description of your app.' },
  { field: 'github_url', question: 'What is the GitHub URL for your app?' },
  { field: 'tags', question: 'What tags describe your app? (comma-separated)' },
  { field: 'image_url', question: 'Optional: Provide an image URL for your app preview.' },
  { field: 'has_crewai', question: 'Does your app use CrewAI? (yes/no)', type: 'boolean' }
];

export default function Submit() {
  const [messages, setMessages] = useState([
    { text: 'Hi! I\'m here to help you submit your agent or app to Awesome Agents. Let\'s start!', sender: 'agent' }
  ]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [input, setInput] = useState('');

  const fetchCodeFromGitHub = async (url) => {
    const match = url.match(/github\.com\/([^\/]+)\/([^\/]+)/);
    if (!match) return null;
    const owner = match[1];
    const repo = match[2];
    try {
      let response = await fetch(`https://api.github.com/repos/${owner}/${repo}/contents/app.py`);
      if (!response.ok) {
        response = await fetch(`https://api.github.com/repos/${owner}/${repo}/contents/streamlit_app.py`);
        if (!response.ok) return null;
      }
      const data = await response.json();
      return atob(data.content);
    } catch (error) {
      return null;
    }
  };

  const upgradeCodeForCrewAI = (code) => {
    let upgradeNotes = "# Added CrewAI support\n";
    let detectedFrameworks = [];

    // Detect frameworks
    if (code.includes('from langgraph') || code.includes('import langgraph')) {
      detectedFrameworks.push('LangGraph');
      upgradeNotes += "# Migration from LangGraph: CrewAI provides similar graph-based orchestration\n";
      upgradeNotes += "# Replace LangGraph StateGraph with CrewAI Crew and Tasks\n";
    }

    if (code.includes('from autogen') || code.includes('import autogen')) {
      detectedFrameworks.push('Microsoft AutoGen');
      upgradeNotes += "# Migration from AutoGen: Use CrewAI agents with similar conversational capabilities\n";
      upgradeNotes += "# AutoGen's AssistantAgent -> CrewAI Agent with role-based configuration\n";
    }

    if (code.includes('from swarm') || code.includes('import swarm')) {
      detectedFrameworks.push('OpenAI Swarm');
      upgradeNotes += "# Migration from Swarm: CrewAI offers more robust multi-agent coordination\n";
      upgradeNotes += "# Swarm's agent switching -> CrewAI's delegation and task assignment\n";
    }

    if (code.includes('from langchain.agents') || code.includes('from langchain_experimental')) {
      detectedFrameworks.push('LangChain Agents');
      upgradeNotes += "# Migration from LangChain Agents: CrewAI provides higher-level agent orchestration\n";
      upgradeNotes += "# LangChain AgentExecutor -> CrewAI Agent with tools integration\n";
    }

    if (code.includes('from vertexai') || code.includes('from google.cloud.aiplatform') || code.includes('google.auth')) {
      detectedFrameworks.push('Google Vertex AI Agents');
      upgradeNotes += "# Migration from Vertex AI: CrewAI works with various LLM providers including Google\n";
      upgradeNotes += "# Vertex AI agents -> CrewAI agents with Google LLM integration\n";
    }

    if (detectedFrameworks.length === 0) {
      upgradeNotes += "# No specific agent frameworks detected - adding general CrewAI integration\n";
    }

    const upgraded = `
from crewai import Agent, Task, Crew
import streamlit as st

# Original code
${code}

${upgradeNotes}
st.header("CrewAI Integration")

# Define agents based on detected frameworks
analyst_agent = Agent(
  role='Data Analyst',
  goal='Analyze data and provide insights for the Streamlit app',
  backstory='You are an expert data analyst integrated into this Streamlit application.',
  allow_delegation=False
)

${detectedFrameworks.includes('Microsoft AutoGen') || detectedFrameworks.includes('OpenAI Swarm') ? `
# For conversational/multi-agent setups (from AutoGen/Swarm migration)
conversational_agent = Agent(
  role='Conversational Assistant',
  goal='Engage in natural conversations and coordinate with other agents',
  backstory='You handle user interactions and coordinate between different AI capabilities.',
  allow_delegation=True
)
` : ''}

${detectedFrameworks.includes('LangChain Agents') ? `
# For tool-using workflows (from LangChain migration)
tool_agent = Agent(
  role='Tool Executor',
  goal='Execute tools and perform actions based on user requests',
  backstory='You can use various tools and APIs to accomplish tasks.',
  allow_delegation=False,
  tools=[]  # Add your tools here
)
` : ''}

${detectedFrameworks.includes('LangGraph') || detectedFrameworks.includes('Google Vertex AI Agents') ? `
# For complex workflows (from LangGraph/Vertex migration)
workflow_agent = Agent(
  role='Workflow Coordinator',
  goal='Manage complex multi-step processes and agent interactions',
  backstory='You orchestrate sophisticated workflows and ensure tasks are completed efficiently.',
  allow_delegation=True
)
` : ''}

# Example tasks
analysis_task = Task(
  description='Analyze the data presented in the app and provide insights.',
  agent=analyst_agent
)

${detectedFrameworks.includes('Microsoft AutoGen') || detectedFrameworks.includes('OpenAI Swarm') ? `
conversation_task = Task(
  description='Handle user conversations and coordinate agent responses.',
  agent=conversational_agent
)
` : ''}

# Crew setup
crew_agents = [analyst_agent]
crew_tasks = [analysis_task]

${detectedFrameworks.includes('Microsoft AutoGen') || detectedFrameworks.includes('OpenAI Swarm') ? `
crew_agents.append(conversational_agent)
crew_tasks.append(conversation_task)
` : ''}

${detectedFrameworks.includes('LangChain Agents') ? `
crew_agents.append(tool_agent)
crew_tasks.append(Task(description='Execute tools and perform actions.', agent=tool_agent))
` : ''}

${detectedFrameworks.includes('LangGraph') || detectedFrameworks.includes('Google Vertex AI Agents') ? `
crew_agents.append(workflow_agent)
crew_tasks.append(Task(description='Coordinate complex workflows.', agent=workflow_agent))
` : ''}

crew = Crew(agents=crew_agents, tasks=crew_tasks)

if st.button('Run CrewAI Analysis'):
    result = crew.kickoff()
    st.write(result)

${detectedFrameworks.length > 0 ? `
st.info("Migration Notes: Your app has been upgraded from ${detectedFrameworks.join(', ')} to CrewAI. Review the code above and adjust agent configurations as needed.")
` : ''}
`;
    return upgraded;
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const newMessages = [...messages, { text: input, sender: 'user' }];
    setMessages(newMessages);

    // Handle boolean fields
    let answerValue = input;
    if (questions[currentQuestion].type === 'boolean') {
      answerValue = input.toLowerCase() === 'yes' || input.toLowerCase() === 'y' ? 1 : 0;
    }

    setAnswers({ ...answers, [questions[currentQuestion].field]: answerValue });

    if (questions[currentQuestion].field === 'github_url') {
      // Fetch and review code
      setMessages([...newMessages, { text: 'Let me review your code from GitHub...', sender: 'agent' }]);
      const code = await fetchCodeFromGitHub(input);
      if (code) {
        const upgradedCode = upgradeCodeForCrewAI(code);
        setMessages(prev => [...prev, { text: `I've reviewed your code and upgraded it for CrewAI support. Here's the enhanced version:\n\n\`\`\`python\n${upgradedCode}\n\`\`\``, sender: 'agent' }]);
      } else {
        setMessages(prev => [...prev, { text: 'I couldn\'t fetch your code from GitHub. Please ensure the repo has app.py or streamlit_app.py.', sender: 'agent' }]);
      }
    }

    setInput('');

    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setMessages(prev => [...prev, { text: questions[currentQuestion + 1].question, sender: 'agent' }]);
    } else {
      // Submit the app
      const appData = {
        ...answers,
        watchers: 0,
        views: 0
      };

      try {
        const response = await fetch('/api/apps', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(appData)
        });

        if (response.ok) {
          setMessages(prev => [...prev, { text: 'Great! Your app has been submitted successfully. You can view it in the gallery now.', sender: 'agent' }]);
        } else {
          setMessages(prev => [...prev, { text: 'Sorry, there was an error submitting your app. Please try again.', sender: 'agent' }]);
        }
      } catch (error) {
        setMessages(prev => [...prev, { text: 'Sorry, there was an error submitting your app. Please try again.', sender: 'agent' }]);
      }
    }
  };

  const startOver = () => {
    setMessages([{ text: 'Hi! I\'m here to help you submit your Streamlit app to the gallery. Let\'s start!', sender: 'agent' }]);
    setCurrentQuestion(0);
    setAnswers({});
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto', padding: '20px' }}>
      <h1>Submit Your Streamlit App</h1>
      <div style={{ border: '1px solid #ccc', padding: '10px', height: '400px', overflowY: 'auto', marginBottom: '10px' }}>
        {messages.map((msg, index) => (
          <div key={index} style={{ marginBottom: '10px', textAlign: msg.sender === 'user' ? 'right' : 'left' }}>
            <strong>{msg.sender === 'user' ? 'You' : 'Agent'}:</strong> {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type your answer..."
          style={{ width: '100%', padding: '10px', marginBottom: '10px' }}
          disabled={currentQuestion >= questions.length}
        />
        <button type="submit" disabled={currentQuestion >= questions.length} style={{ padding: '10px 20px' }}>
          Send
        </button>
        <button type="button" onClick={startOver} style={{ padding: '10px 20px', marginLeft: '10px' }}>
          Start Over
        </button>
      </form>
    </div>
  );
}
