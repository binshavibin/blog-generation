
from src.states.blog_state import BlogState
from langchain_core.messages import HumanMessage,SystemMessage
from src.states.blog_state import BlogState,Blog
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

    def translation(self,state:BlogState):
        """
        Translate the content into specific language
        """
        translation_prompt = """
        Translate the following content into {current_language}.
        Maintain original tone,style,formatting
        Original content
        {blog_content}
        """
        blog_content = state['blog']['content']
        messages = [
            HumanMessage(translation_prompt.format(current_language=state['current_language'], blog_content=blog_content))
        ]

        translation_content = self.llm.with_structured_output(Blog).invoke(messages)
        return {"blog":{"title":state['blog']['title'],"content":translation_content.content}}

    def route(self,state:BlogState):
        return {"current_language":state['current_language']}

    def route_decision(self,state:BlogState):
        """
        Route the content to respective language translation.
        """
        if state['current_language']=="hindi":
            return "hindi"
        elif state['current_language']=="french":
            return "french"
        else:
            return state['current_language']
                
