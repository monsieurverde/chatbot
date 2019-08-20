class Chatbot:
    """ An object that can engage in rudimentary conversation with a human. """

    def __init__(self, name):
        self.name = name

    def greeting(self):
        """ Returns the Chatbot's way of introducing itself. """
        return "Hello, my name is " + self.name

    def response(self, prompt_from_human):
        """ Returns the Chatbot's response to something the human said. """
        return "It is very interesting that you say: '" + prompt_from_human + "'"

class BoredChatbot(Chatbot):

    def __init__(self, name):
        Chatbot.__init__(self, name)
        # then set the name attribute
        self.name = name 
    
    def response(self, prompt_from_human):
        length_prompt = len(prompt_from_human)
        if length_prompt > 20:
            return "zzz... Oh excuse me, I dozed off reading your essay."
        else:
            return Chatbot.response(self,prompt_from_human)