# 1st method
# TEMPLATE = """
# Hello {name}
# """

# def main():
#     print(TEMPLATE.format(name = "ram"))

# main()
# if __name__ == "__main__":
#     main()

# # ALTERNATIVE => 
# TEMPLATE = """
# Hello {0}
# """

# def main():
#     print(TEMPLATE.format("ram"))

# if __name__ == "__main__":
#     main()


# Alternative =>
# def main():
#     name = "Thej"
#     # इसे f-string कहते हैं, इसमें सीधा वेरिएबल का नाम {} के अंदर आ जाता है
#     print(f"Hello {name}")

# if __name__ == "__main__":
#     main()


# 💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡💡

# from jinja2 import Template
# TEMPLATE = """ Hello {{ name }} !"""
# def main():
#     template = Template(TEMPLATE)
#     print(template.render(name='Thej'))

# if __name__ == "__main__":
#     main()

# YE DEKHO KYA CUSTOM AUR KYA SPECIFIC NAME HAIN =>
# 1. Template (बड़ा T) SPECIFIC है, इसे नहीं बदल सकते
from jinja2 import Template 

# 2. my_raw_text हमारा CUSTOM नाम है (हमने TEMPLATE बदल दिया)
my_raw_text = """ Hello {{ name }} !""" 

def main():
    # 3. my_ready_sancha हमारा CUSTOM नाम है (हमने छोटे template को बदल दिया)
    my_ready_sancha = Template(my_raw_text) 
    
    # 4. अब इसे रन कर रहे हैं
    print(my_ready_sancha.render(name='Thej'))

if __name__ == "__main__":
    main()

















