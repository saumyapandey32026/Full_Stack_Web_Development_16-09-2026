# 1. SPECIFIC NAME (जिन्जा का फिक्स्ड टूल, इसे बदल नहीं सकते)
# काम: जिन्जा लाइब्रेरी से Template नाम का मुख्य इंजन इम्पोर्ट किया गया है।
from jinja2 import Template

janapith_data = {
    "year": 1965, 
    "awardees": "G. Sankara Kurup", 
    "language": "Malayalam"
}

# 3. CUSTOM NAME (आपका अपना वेरिएबल)
# काम: प्रोफेसर ने ट्रिपल कोट्स (""") का उपयोग करके पूरी HTML इसी के अंदर लिख दी।
# पायथन के लिए यह सिर्फ एक बड़ा टेक्स्ट है।
TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8"/>
    <title> Jnanpith </title>
    <meta name="description" content="This page lists Jnanpith Awardees"/>
</head>
<body>
    <h1> Awardees </h1>
    <table>
        <thead>
            <tr>
                <th>Year</th>
                <th>Awardees</th>
                <th>Language</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                # <!-- जिन्जा का कमाल: यहाँ HTML के अंदर डेटा निकाला जा रहा है -->
                # <!-- janapith_data["year"] लिखने से यहाँ 1965 आ जाएगा -->
                <td>{{ janapith_data["year"] }}</td>
                
                # <!-- janapith_data["awardees"] लिखने से यहाँ नाम आ जाएगा -->
                <td>{{ janapith_data["awardees"] }}</td>
                
                # <!-- janapith_data["language"] लिखने से यहाँ Malayalam आ जाएगा -->
                <td>{{ janapith_data["language"] }}</td>
            </tr>
        </tbody>
    </table>
</body>
</html>
"""

# 4. SPECIFIC NAME (पायथन का फंक्शन बनाने का तरीका)
def main():
    # 5. CUSTOM NAME = SPECIFIC TOOL (CUSTOM VARIABLE)
    # काम: जिन्जा के इंजन (Template) को हमारा HTML वाला बड़ा टेक्स्ट (TEMPLATE) सौंप दिया गया।
    template = Template(TEMPLATE)
    
    # 6. SPECIFIC FUNCTION (जिन्जा का फिक्स्ड काम करने वाला फंक्शन)
    # काम: .render() फंक्शन ने janapith_data नाम के वेरिएबल को जिन्जा के सांचे में भेज दिया।
    # इसके बाद जिन्जा ने HTML के अंदर मौजूद {{ ... }} को असली डेटा से बदल दिया।
    print(template.render(janapith_data=janapith_data))

# 7. SPECIFIC CONDITION (पायथन का फिक्स्ड सुरक्षा गार्ड)
if __name__ == "__main__":
    main()
