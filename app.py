from dotenv import load_dotenv
from langchain_openai import OpenAI


async def llm_call(llm):
    async for chunk in llm.astream(
        "What are some theories about the relationship between unemployment and inflation?"
    ):
        print(chunk, end="", flush=True)


def main():
    load_dotenv('.env')
    llm = OpenAI(
        model="gpt-3.5-turbo-instruct",
        max_tokens=512,
        temperature=0
    )

    import asyncio
    asyncio.run(llm_call(llm))


if __name__ == "__main__":
    main()


"""
1. tried invoke: sending the response as a string at once, you have to wait.
2. stream: sending the response as a chunk of string, you can see the response as it comes.
3. batch: sending the response as a list of string, it's same as invoke.
4. astream: sending the response as a async generator of string, you can see the response as it comes.
5. the async is faster than the sync.
"""
