import streamlit as st

def rk(string, pattern, d, p):
    hash_s = 0
    hash_p = 0
    len_s = len(string)
    len_p = len(pattern)
    h = pow(d, len_p-1, p)
    
    output = ""

    for i in range(len(pattern)):
        hash_s = (d*hash_s + ord(string[i]))%p
        hash_p = (d*hash_p + ord(pattern[i]))%p

    
    output += f"n = {len_s}\nm = {len_p}\nh = {d}**{len_p-1} mod {p} = {h}\nHash of Pattern = {hash_p}\nHash of Sub-String = {hash_s}\n"
    output += f"[{string[0:len_p]}]{string[len_p:]} || "
    output += f"Hash = {hash_s}\n"

    for i in range(len_s - len_p+1):
        if hash_p == hash_s:
            output += "HASH MATCH FOUND!\n"
            if string[i:i+len_p] == pattern:
                output += f"Pattern Matches INDEX {i, i+len_p-1}\n"
            else:
                output += "STRING DID NOT MATCH\n"
        try:
            output += f"{string[0:i+1]}[{string[i+1:i+len_p+1]}]{string[i+1+len_p:]} || "
            output += f"({d}*({hash_s}-{ord(string[i])}*{h}) + {ord(string[i+len_p])})%{p} = "
            hash_s = (d*(hash_s - ord(string[i])*h) + ord(string[i+len_p]) )%p
            if hash_s < 0: 
                hash_s = (hash_s + p)%p
            output += str(hash_s)+"\n"
        except IndexError:
            pass
        
    return output



with st.form("rbk_inputs"):
    string = st.text_input("Enter String")
    pattern = st.text_input("Enter Pattern String")
    d = st.text_input("Enter d (Default = 256)")
    p = st.text_input("Enter prime number")
    
    submitted = st.form_submit_button("Submit")
    
    if submitted:
        st.code(rk(string, pattern, int(d), int(p)))
    