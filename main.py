from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
#Estos son para que el output del modelo siga un formato especifico y no se pierda en el prompt
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, save_tool

load_dotenv()

#Modelo base de salida.
class ResearchResponse(BaseModel):
    #especificamos el formato de salida que queremos que tenga el modelo, para que no se pierda en el prompt
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm = ChatAnthropic(model="claude-haiku-5-5")
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            #Estos es informacion que le damos al modelo para que sepa como debe comportarse y que formato de salida debe tener
            "system",
                        """
            You are a research assistant that will help generate a research paper.
            Answer the user query and use neccessary tools.
            ALWAYS use the save_text_to_file tool before giving your final answer,
            passing the full research result as the data argument.
            Wrap the final output in this format and provide no other text\n{format_instructions}
            """,

        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
).partial(format_instructions=parser.get_format_instructions())

tools= [search_tool, save_tool]

agent = create_tool_calling_agent(
llm=llm,
prompt=prompt,
tools=tools
)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

query = input("What can i help you research? ")
raw_response =  agent_executor.invoke({"query": query})
print(raw_response)

try:
    text = next(b["text"] for b in raw_response["output"] if b["type"] == "text")
    structured_response = parser.parse(text)
    print(structured_response)
except Exception as e:
    print("Error parsing response", e,"Raw response:" ,raw_response)

