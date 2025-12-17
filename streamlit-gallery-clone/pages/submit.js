import { useState } from 'react';

const questions = [
  { field: 'title', question: 'What is the title of your Streamlit app?' },
  { field: 'description', question: 'Please provide a brief description of your app.' },
  { field: 'github_url', question: 'What is the GitHub URL for your app?' },
  { field: 'tags', question: 'What tags describe your app? (comma-separated)' },
  { field: 'image_url', question: 'Optional: Provide an image URL for your app preview.' }
];

export default function Submit() {
  const [messages, setMessages] = useState([
    { text: 'Hi! I\'m here to help you submit your Streamlit app to the gallery. Let\'s start!', sender: 'agent' }
  ]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [answers, setAnswers] = useState({});
  const [input, setInput] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;

    const newMessages = [...messages, { text: input, sender: 'user' }];
    setMessages(newMessages);
    setAnswers({ ...answers, [questions[currentQuestion].field]: input });
    setInput('');

    if (currentQuestion < questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setMessages([...newMessages, { text: questions[currentQuestion + 1].question, sender: 'agent' }]);
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
          setMessages([...newMessages, { text: 'Great! Your app has been submitted successfully. You can view it in the gallery now.', sender: 'agent' }]);
        } else {
          setMessages([...newMessages, { text: 'Sorry, there was an error submitting your app. Please try again.', sender: 'agent' }]);
        }
      } catch (error) {
        setMessages([...newMessages, { text: 'Sorry, there was an error submitting your app. Please try again.', sender: 'agent' }]);
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
