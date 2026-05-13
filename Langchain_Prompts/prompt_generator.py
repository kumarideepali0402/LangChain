from langchain_core.prompts import PromptTemplate

template = PromptTemplate(
    template=""" 
    Summarize this paper titled"{paper_input} in a style "{style_input}" which has length
    of"{length_input}"
    
    """,
    input_variables=['paper_input', 'style_input', 'length_input'],
    validate_template = True
    
)

template.save('template.json')