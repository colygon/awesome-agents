"""CRM Q&A Agent - CrewAI Multi-Agent CRM Question Answering System"""
import os, sys
from datetime import datetime
from dotenv import load_dotenv
from crewai import Crew, Process
from agents import create_query_interpreter, create_data_retriever, create_answer_synthesizer
from tasks import create_query_interpretation_task, create_data_retrieval_task, create_answer_synthesis_task

def load_environment():
    load_dotenv()
    if not os.getenv('OPENAI_API_KEY'):
        print("ERROR: OPENAI_API_KEY not found.")
        sys.exit(1)

def run_crm_qa(user_question: str):
    interpreter = create_query_interpreter()
    retriever = create_data_retriever()
    synthesizer = create_answer_synthesizer()

    interpretation_task = create_query_interpretation_task(interpreter, user_question)
    retrieval_task = create_data_retrieval_task(retriever, interpretation_task)
    synthesis_task = create_answer_synthesis_task(synthesizer, interpretation_task, retrieval_task, user_question)

    crew = Crew(agents=[interpreter, retriever, synthesizer], tasks=[interpretation_task, retrieval_task, synthesis_task], process=Process.sequential, verbose=True)
    return {'result': crew.kickoff(), 'timestamp': datetime.now().isoformat()}

def main():
    load_environment()
    result = run_crm_qa("What are the top 10 customers by revenue this quarter?")
    print(f"\n\nCRM Q&A RESULTS\n{result['result']}")

if __name__ == "__main__":
    main()
