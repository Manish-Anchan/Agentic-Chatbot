from tavily import TavilyClient
from langchain.prompts import ChatPromptTemplate


class AINewsNode:
    def __init__(self, llm):
        self.llm = llm
        self.tavily = TavilyClient()

        self.state = {}

    def fetch_news(self, state: dict) -> dict:
        """
        Fetch AI news based on the specified frequency.
        
        Args:
            state (dict): The state dictionary containing 'frequency'.
        
        Returns:
            dict: Updated state with 'news_data' key containing fetched news.
        """

        frequency = state['messages'][0].content.lower()
        self.state['frequency'] = frequency
        time_range_map = {'daily': 'd', 'weekly': 'w', 'monthly': 'm', 'year': 'y'}
        days_map = {'daily': 1, 'weekly': 7, 'monthly': 30, 'year': 366}

        response = self.tavily.search(
            query="Top Artificial Intelligence (AI) technology news India and globally",
            topic="news",
            time_range=time_range_map[frequency],
            include_answer="advanced",
            max_results=20,
            days=days_map[frequency],
        
        )

        state['news_data'] = response.get('results', [])
        self.state['news_data'] = state['news_data']
        return state
    
    
    def summarize_news(self, state: dict) -> dict:
        
        news_items = self.state['news_data']

        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are an expert AI news summarizer. Summarize AI-related news articles into markdown format. 

        Requirements:
        - Date in **YYYY-MM-DD** (IST timezone)
        - 2–3 sentence summary with key details (not just title)
        - Must include source as hyperlink
        - Sort by date (latest first)

        Format:
        ### [Date]
        - [Summary text](URL)"""),
            ("user", "Articles:\n{articles}")
        ])

        
        articles_str = "\n\n".join([
            f"Title: {item.get('title', '')}\n"
            f"Content: {item.get('content', '')}\n"
            f"URL: {item.get('url', '')}\n"
            f"Date: {item.get('published_date', '')}"
            for item in news_items
        ])


        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state['summary'] = response.content
        self.state['summary'] = state['summary']
        return self.state
        

    def save_result(self,state):
        frequency = self.state['frequency']
        summary = self.state['summary']
        filename = f"./AINews/{frequency}_summary.md"
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary\n\n")
            f.write(summary)
        self.state['filename'] = filename
        return self.state
