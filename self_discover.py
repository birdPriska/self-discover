"""
An implementation of SELF-DISCOVER: Large Language Models Self-Compose Reasoning 
Structures, https://arxiv.org/pdf/2402.03620.pdf

Coarse structure:
    STAGE 1
    1. SELECT: Select relevant reasoning modules for the task.
    2. ADAPT: Adapt the selected reasoning modules to be more specific to the task.
    3. IMPLEMENT: Implement the adapted reasoning modules into an actionable reasoning structure.
    STAGE 2
    4. EXECUTE: Execute the reasoning structure to solve a specific task instance.

Adapted from https://github.com/catid/self-discover/

Usage:
    Pick a language model to use for prompting and make sure you have a relevant API key
    stored in a .env file somewhere, then run
    `python self_discover.py`

Example task:
    A motorboat going downstream overcame a raft at a point A; t = 60 min later it 
    turned back and after some time passed the raft at a distance l = 6.0 km from the 
    point A. Find the flow velocity assuming the duty of the engine to be constant.
    (Problem 1.1. from "Problems in General Physics" by I. E. Irodov)

"""

from dotenv import load_dotenv, find_dotenv

# from langchain_openai import ChatOpenAI
from langchain_mistralai.chat_models import ChatMistralAI


# get the API key from an .env file
load_dotenv(find_dotenv())

# instantiate the LLM client
# client = ChatOpenAI(model_name="gpt-4-turbo-preview", temperature=0.1, max_tokens=2048)
client = ChatMistralAI(model_name="mistral-medium", temperature=0.1, max_tokens=2048)


def query_llm(prompt):
    """
    Query the language model with a given prompt.
    """
    response = client.invoke(prompt)
    return response.content


# STAGE 1


def select(task, reasoning_modules):
    """
    Step 1: SELECT relevant reasoning modules for the task.
    """
    prompt = f"""Select several reasoning modules that are crucial to utilize in order
    to solve the given task:

    All reasoning modules descriptions:
    {reasoning_modules}

    Task examples w/o answers:
    - Example 1: {task}

    Select several modules that are crucial for solving the task above:
    """
    selected_modules = query_llm(prompt)
    return selected_modules


def adapt(task, selected_modules):
    """
    Step 2: ADAPT the selected reasoning modules to be more specific to the task.
    """
    prompt = f"""Rephrase and specify each reasoning module so that it better helps
    solving the task:

    SELECTED module descriptions:
    {selected_modules}

    Task examples w/o answers:
    - Example 1: {task}

    Adapt each reasoning module description to better solve the tasks:
    """

    adapted_modules = query_llm(prompt)
    return adapted_modules


def implement(task, adapted_modules, reasoning_structure_example):
    """
    Step 3: IMPLEMENT the adapted reasoning modules into an actionable reasoning structure.

    TODO: add
    Reasoning description example: {reasoning_description_example}
    Reasoning plan example: {reasoning_structure_example}
    """
    prompt = f"""Operationalize the reasoning modules into a step-by-step reasoning plan
    in JSON format:

    Reasoning structure example: {reasoning_structure_example}
    
    ADAPTED module descriptions:
    {adapted_modules}

    Task examples w/o answers:
    - Example 1: {task}

    Implement a reasoning structure for solvers to follow step-by-step and arrive at 
    correct answers:
    """

    reasoning_structure = query_llm(prompt)
    return reasoning_structure


# STAGE 2


def execute(task, reasoning_plan):
    """
    EXECUTE the reasoning plan to solve a specific task instance.
    """
    prompt = f"""Follow the step-by-step reasoning plan in JSON to correctly solve the 
    task. Fill in the values following the keys by reasoning specifically about the task
    given. Do not simply rephrase the keys.

    Reasoning plan: {reasoning_plan}

    Task: {task}
    """
    solution = query_llm(prompt)
    return solution


if __name__ == "__main__":

    reasoning_modules = [
        "1. How could I devise an experiment to help solve that problem?",
        "2. Make a list of ideas for solving this problem, and apply them one by one to the problem to see if any progress can be made.",
        "3. How could I measure progress on this problem?",
        "4. How can I simplify the problem so that it is easier to solve?",
        "5. What are the key assumptions underlying this problem?",
        "6. What are the potential risks and drawbacks of each solution?",
        "7. What are the alternative perspectives or viewpoints on this problem?",
        "8. What are the long-term implications of this problem and its solutions?",
        "9. How can I break down this problem into smaller, more manageable parts?",
        "10. Critical Thinking: This style involves analyzing the problem from different perspectives, questioning assumptions, and evaluating the evidence or information available. It focuses on logical reasoning, evidence-based decision-making, and identifying potential biases or flaws in thinking.",
        "11. Try creative thinking, generate innovative and out-of-the-box ideas to solve the problem. Explore unconventional solutions, thinking beyond traditional boundaries, and encouraging imagination and originality.",
        "12. Seek input and collaboration from others to solve the problem. Emphasize teamwork, open communication, and leveraging the diverse perspectives and expertise of a group to come up with effective solutions.",
        "13. Use systems thinking: Consider the problem as part of a larger system and understanding the interconnectedness of various elements. Focuses on identifying the underlying causes, feedback loops, and interdependencies that influence the problem, and developing holistic solutions that address the system as a whole.",
        "14. Use Risk Analysis: Evaluate potential risks, uncertainties, and tradeoffs associated with different solutions or approaches to a problem. Emphasize assessing the potential consequences and likelihood of success or failure, and making informed decisions based on a balanced analysis of risks and benefits.",
        "15. Use Reflective Thinking: Step back from the problem, take the time for introspection and self-reflection. Examine personal biases, assumptions, and mental models that may influence problem-solving, and being open to learning from past experiences to improve future approaches.",
        "16. What is the core issue or problem that needs to be addressed?",
        "17. What are the underlying causes or factors contributing to the problem?",
        "18. Are there any potential solutions or strategies that have been tried before? If yes, what were the outcomes and lessons learned?",
        "19. What are the potential obstacles or challenges that might arise in solving this problem?",
        "20. Are there any relevant data or information that can provide insights into the problem? If yes, what data sources are available, and how can they be analyzed?",
        "21. Are there any stakeholders or individuals who are directly affected by the problem? What are their perspectives and needs?",
        "22. What resources (financial, human, technological, etc.) are needed to tackle the problem effectively?",
        "23. How can progress or success in solving the problem be measured or evaluated?",
        "24. What indicators or metrics can be used?",
        "25. Is the problem a technical or practical one that requires a specific expertise or skill set? Or is it more of a conceptual or theoretical problem?",
        "26. Does the problem involve a physical constraint, such as limited resources, infrastructure, or space?",
        "27. Is the problem related to human behavior, such as a social, cultural, or psychological issue?",
        "28. Does the problem involve decision-making or planning, where choices need to be made under uncertainty or with competing objectives?",
        "29. Is the problem an analytical one that requires data analysis, modeling, or optimization techniques?",
        "30. Is the problem a design challenge that requires creative solutions and innovation?",
        "31. Does the problem require addressing systemic or structural issues rather than just individual instances?",
        "32. Is the problem time-sensitive or urgent, requiring immediate attention and action?",
        "33. What kinds of solution typically are produced for this kind of problem specification?",
        "34. Given the problem specification and the current best solution, have a guess about other possible solutions."
        "35. Let's imagine the current best solution is totally wrong, what other ways are there to think about the problem specification?"
        "36. What is the best way to modify this current best solution, given what you know about these kinds of problem specification?"
        "37. Ignoring the current best solution, create an entirely new solution to the problem."
        "38. Let's think step by step."
        "39. Let's make a step by step plan and implement it with good notation and explanation.",
    ]

    reasoning_structure_example = """{
        "Simplify SVG path": "..",
        "Breakdown of path commands": {
            "..": "..",
            "..": ".."
        },
        "Critical thinking analysis": {
            "Logical reasoning": {
                "..": "..",
                "..": ".."
            },
        },
        "Final reasoning and decision": "..",
        "Final answer": ".."
    }
    """

    # get the task description from standard input
    task = input("Enter the task description: ")

    print("STAGE 1")
    selected_modules = select(task, reasoning_modules)
    print(f"SELECT: \n{selected_modules}\n")

    adapted_modules = adapt(task, selected_modules)
    print(f"ADAPT: \n{adapted_modules}\n")

    reasoning_structure = implement(task, adapted_modules, reasoning_structure_example)
    print(f"IMPLEMENT: \n{reasoning_structure}\n")

    print("STAGE 2")
    result = execute(task, reasoning_structure)
    print(f"OUTPUT: \n{result}")
