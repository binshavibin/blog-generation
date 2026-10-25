
from src.states.blog_state import BlogState
class BlogNode:
    """
    A class to represent blog node
    """

    def __init__(self,llm):
        self.llm = llm

    def title_creation(self,state:BlogState):
        """
        create title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt ="""
                    You are an export content creator.Use markdown formatting .Generate blog title for the {topic}.
                    The title should be created seo friendly.
                    """
            system_message =prompt.format(topic=state['topic'])
            response  = self.llm.invoke(system_message)
            return {"blog":{"title":response.content}}

    def content_generation(self,state:BlogState):
            """
            create content for the blog
            """
    
            if "topic" in state and state["topic"]:
                prompt ="""
                        You are an export content creator.Use markdown formatting .
                        Generate blog content for the {topic}.
                        The content should be related to the topic.
                        """
                system_message =prompt.format(topic=state['topic'])
                response  = self.llm.invoke(system_message)
                return {"blog":{"title":state['blog']['title'],'content':response.content}}
