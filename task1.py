import streamlit as st
from simpleai.search import CspProblem, backtrack

st.title("Task 1: Cryptarithmetic Puzzle")
st.write("  ")
st.write("  ")
col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    term1_input = st.text_input("Enter first term: ").upper()

with col2:
    st.write("  ")
    st.subheader("+",anchor=False)
with col3:
    term2_input = st.text_input("Enter second term: ").upper()

with col4:
    st.write("  ")
    st.subheader("=",anchor=False)

with col5:
    result_input = st.text_input("Enter the result: ").upper()



def letters_list(input_string):
    # Use a list comprehension to extract letters from the input string
    letter_list = [char for char in input_string if char.isalpha()]
    return letter_list

letters = letters_list(term1_input + term2_input + result_input)
variables = set(letters)

with col3:
    st.write("  ")
    button = st.button("Solve!",use_container_width=True)


if button:
    domains = {
        term1_input[0]: list(range(1, 10)),
        term2_input[0]: list(range(1, 10)),
        result_input[0]: list(range(1, 10)),
    }
    for letter in variables:
        domains.setdefault(letter,list(range(0, 10)))


    def constraint_unique(variables, values):
        return len(values) == len(set(values))  # remove repeated values and count

    def constraint_add(variables, values):
        term1 = ""
        for i in range(0,len(term1_input)):
            term1 += str(values[i]) # value of the letter
        term1 = int(term1)

        term2 = ""
        term2_limit = len(term1_input) + len(term2_input) #
        for i in range(len(term1_input),term2_limit):
            term2 += str(values[i]) # value of the letter
        
        term2 = int(term2)

        result = ""
        result_limit = term2_limit + len(result_input)
        for i in range(term2_limit,result_limit):
            result += str(values[i]) # value of the letter
        result = int(result)

        return (term1 + term2) == result

    constraints = [
        (variables, constraint_unique),
        (letters, constraint_add),
    ]
    st.write("  ")
    st.write("  ")
    st.write("  ")
    st.write("  ")
    st.write("  ")

    problem = CspProblem(variables, domains, constraints)
    output = backtrack(problem)
    number1 = ""
    for i in range(0,len(term1_input)):
        number1 += str(output[term1_input[i]])
    
    number2 = ""
    for i in range(0,len(term2_input)):
        number2 += str(output[term2_input[i]])
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.write(' ')
        st.header("+")
        
    with col2:
        st.write(' ')
    with col3:
        st.header(term1_input, anchor=False)
        st.header(term2_input, anchor=False)

    with col4:
        st.write(' ')
    with col5:
        st.header(number1,anchor=False)
        st.header(number2,anchor=False)
    st.divider()
    col1,col2,col3,col4,col5 = st.columns(5)
    number3 = ""
    for i in range(0,len(result_input)):
        number3 += str(output[result_input[i]])
    with col1:
        st.write(' ')
    with col2:
        st.write(' ')
    with col3:
        st.header(result_input, anchor=False)

    with col4:
        st.write(' ')
    with col5:
        st.header(number3,anchor=False)

footer="""<style>
.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: white;
color: black;
text-align: center;
}
</style>
<div class="footer">
<p>Made by Chadi Abdelghani-Idrissi</p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)