# -*- coding: utf-8 -*-
import requests
import openai
import json
import datetime

openai.api_key = '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'

URL = "https://api.openai.com/v1/chat/completions"



def wishMe():
    hour=int(datetime.datetime.now().hour)
    if(lang=='english'):
        if(hour>=5 and hour<12):
            print("Good Morning , How can i help you")
        elif(hour>=12 and hour<=16):
            print("Good afternoon , How can i help you")
        else:
            print("Good evening , How can i help you")
    elif(lang=='tamilh'):
        if(hour>=5 and hour<12):
            print("Good Morning "+" How can i help you")
        elif(hour>=12 and hour<=16):
            print("Good afternoon "+" How can i help you")
        else:
            print("Good evening "+" How can i help you")
    else:
        if(hour>=5 and hour<12):
            print("सुप्रभात मैं आपकी कैसे साहायता कर सकता हूँ")
        elif(hour>=12 and hour<=16):
            print("नमस्कार मैं आपकी कैसे साहायता कर सकता हूँ")
        else:
            print("नमस्ते मैं आपकी कैसे साहायता कर सकता हूँ")

def drought():
    eng_sol=['You can Use Plant species and varieties of crops that withstand dryness, hold water, and reduce the need for irrigation.  Melons, tomatoes, squash and beans are better suited to dry conditions',
             'You can Use conservation practices that reduce runoff and encourage the infiltration of water into the soil',
             'You can Leave crop residue in your field to improve the water-holding capacity of your soil and reduce evaporation and erosion',
             'You can Use Drip irrigation that has the potential to save water and nutrients by allowing water to drip slowly to the roots of plants, either from above the soil surface or buried below the surface']
    
    hin_sol=['आप आप उन पौधों की प्रजातियों और फसलों की किस्मों का उपयोग कर सकते हैं जो सूखापन का सामना करती हैं, पानी को रोके रखती हैं और सिंचाई की आवश्यकता को कम करती हैं। खरबूजे, टमाटर, स्क्वैश और बीन्स शुष्क परिस्थितियों के लिए बेहतर अनुकूल हैं',
             'आप आप संरक्षण प्रथाओं का उपयोग कर सकते हैं जो अपवाह को कम करती हैं और मिट्टी में पानी की घुसपैठ को प्रोत्साहित करती हैं',
             'आप आप अपनी मिट्टी की जल-धारण क्षमता में सुधार करने और वाष्पीकरण और क्षरण को कम करने के लिए अपने खेत में फसल अवशेषों को छोड़ सकते हैं',
             'आप आप ड्रिप सिंचाई का उपयोग कर सकते हैं जिसमें मिट्टी की सतह के ऊपर से या सतह के नीचे दबे पानी को पौधों की जड़ों तक धीरे-धीरे टपकने की अनुमति देकर पानी और पोषक तत्वों को बचाने की क्षमता है।']
    
    tam_sol=['வறட்சியைத் வறட்சியைத் தாங்கும், தண்ணீரைத் தாங்கும் மற்றும் நீர்ப்பாசனத்தின் தேவையைக் குறைக்கும் தாவரங்கள் மற்றும் பயிர்களின் வகைகளை நீங்கள் பயன்படுத்தலாம். முலாம்பழம், தக்காளி, ஸ்குவாஷ் மற்றும் பீன்ஸ் ஆகியவை வறண்ட நிலைமைகளுக்கு மிகவும் பொருத்தமானவை',
             'நீரோட்டத்தை நீரோட்டத்தை குறைக்கும் மற்றும் மண்ணில் நீர் ஊடுருவுவதை ஊக்குவிக்கும் பாதுகாப்பு நடைமுறைகளை நீங்கள் பயன்படுத்தலாம்',
             'உங்கள் உங்கள் மண்ணின் நீர்ப்பிடிப்புத் திறனை மேம்படுத்தவும், ஆவியாதல் மற்றும் அரிப்பைக் குறைக்கவும் பயிர் எச்சங்களை உங்கள் வயலில் விடலாம்.',
             'மண்ணின் மண்ணின் மேற்பரப்பிலிருந்து அல்லது மேற்பரப்பிற்கு கீழே புதைக்கப்பட்ட தாவரங்களின் வேர்களுக்கு மெதுவாக நீர் சொட்ட அனுமதிப்பதன் மூலம் நீர் மற்றும் ஊட்டச்சத்துக்களை சேமிக்கும் திறன் கொண்ட சொட்டு நீர் பாசனத்தைப் பயன்படுத்தலாம்.']
    if(lang=='tamil'):
        print(tam_sol)
    elif(lang=='english'):
        print(eng_sol)
    else:
        print(hin_sol)


def fertility():
    eng_sol=['you can plant Leguminous plants, which include peas, beans, clover, gorse, acacia, and carob, are a group of flowering plants with pods (or vegetables) as foods grown from the ground knobs, enabling the capacity of nitrogen-rich material.',
             'Rotating in high-residue crops — such as corn, hay, and small grain — can reduce erosion as the layer of residue protects topsoil from being carried away by wind and water.',
             'Adding manure or fertilizers can increse the fertilty of soil but not in exccess as it can cause unfertility of soil in future or pollutions in nearby waterbodies']   

    hin_sol=['आप फलीदार पौधों को लगा सकते हैं, जिसमें मटर, सेम, तिपतिया घास, गोरस, बबूल, और कैरब शामिल हैं, फली (या सब्जियों) के साथ फूलों के पौधों का एक समूह है, जो कि जमीन की गांठों से उगाए गए खाद्य पदार्थ हैं, जो नाइट्रोजन युक्त सामग्री की क्षमता को सक्षम करते हैं।',
             'उच्च अवशेष वाली फसलों - जैसे मकई, घास, और छोटे अनाज - में सड़ने से कटाव कम हो सकता है क्योंकि अवशेषों की परत ऊपरी मिट्टी को हवा और पानी से दूर ले जाने से बचाती है',
             'खाद या उर्वरक डालने से मिट्टी की उर्वरता बढ़ सकती है लेकिन अधिक मात्रा में नहीं क्योंकि यह भविष्य में मिट्टी की उर्वरता या आस-पास के जल निकायों में प्रदूषण का कारण बन सकता है।']

    tam_sol=['பட்டாணி, பீன்ஸ், க்ளோவர், கோர்ஸ், அகாசியா மற்றும் கரோப் உள்ளிட்ட பயறு வகை தாவரங்களை நீங்கள் நடலாம்',
             'மக்காச்சோளம், வைக்கோல் மற்றும் சிறு தானியங்கள் போன்ற அதிக எச்சம் உள்ள பயிர்களில் சுழற்றுவது அரிப்பைக் குறைக்கும், ஏனெனில் எச்சத்தின் அடுக்கு மேல் மண்ணை காற்று மற்றும் நீரால் எடுத்துச் செல்லப்படாமல் பாதுகாக்கிறது',
             'உரம் அல்லது உரங்களைச் சேர்ப்பது மண்ணின் வளத்தை அதிகரிக்கலாம் ஆனால் மிகையாகாது, ஏனெனில் இது எதிர்காலத்தில் மண்ணின் மலட்டுத்தன்மையை அல்லது அருகிலுள்ள நீர்நிலைகளில் மாசுபாட்டை ஏற்படுத்தும்.']
    
    if(lang=='tamil'):
        print(tam_sol)
    elif(lang=='english'):
        print(eng_sol)
    else:
        print(hin_sol)



def money():
    eng_sol = ['Irrigation facilities can help you grow crops year-round, increasing their productivity and income. The government can provide subsidies for irrigation equipment or partner with private companies to develop irrigation facilities in rural areas.',
               'Kisan Credit Card Scheme: This scheme provides farmers with access to short-term credit at low-interest rates to meet their agricultural and other allied activities financial requirements.',
               'Price stabilization measures: Farmers often struggle to get fair prices for their crops due to fluctuating market prices. Implementing price stabilization measures, such as minimum support prices, can provide farmers with a stable income and reduce their financial risk',
               'Pradhan Mantri Krishi Sinchai Yojana: This scheme aims to improve farm productivity by providing irrigation facilities, promoting efficient water use, and developing water conservation infrastructure in rural areas.']
    
    hin_sol = ['सिंचाई सुविधाओं से किसानों को साल भर फसल उगाने में मदद मिल सकती है, जिससे उनकी उत्पादकता और आमदानी में वृद्धि हो सकती है। सरकार ग्रामीण क्षेत्रों में सिंचाई सुविधाओं को विकसित करने के लिए सिंचाई उपकरणों के लिए सब्सिडी प्रदान कर सकती है या निजी कंपनियों के साथ साझेदारी कर सकती है',
               'किसान क्रेडिट कार्ड योजना: यह योजना किसानों को उनकी कृषि और अन्य संबद्ध गतिविधियों की वित्तीय आवश्यकताओं को पूरा करने के लिए कम ब्याज दरों पर अल्पकालिक ऋण तक पहुंच प्रदान करती है',
               'मूल्य स्थिरीकरण: बाजार की कीमतों में उतार-चढ़ाव के कारण किसान अक्सर अपनी फसलों के उचित मूल्य प्राप्त करने के लिए संघर्ष करते हैं। मूल्य स्थिरीकरण उपायों को लागू करना, जैसे न्यूनतम समर्थन मूल्य, किसानों को स्थिर आय प्रदान कर सकते हैं और उनके वित्तीय जोखिम को कम कर सकते हैंS',
               'प्रधानमंत्री कृषि सिंचाई योजना: इस योजना का उद्देश्य ग्रामीण क्षेत्रों में सिंचाई सुविधाएं प्रदान करके, कुशल जल उपयोग को बढ़ावा देना और जल संरक्षण बुनियादी ढांचे का विकास करके कृषि उत्पादकता में सुधार करना है']

    tam_sol = ['நீர்ப்பாசன வசதிகள் ஆண்டு முழுவதும் பயிர்களை வளர்த்து, அவற்றின் உற்பத்தித்திறனையும் வருமானத்தையும் அதிகரிக்க உதவும். நீர்ப்பாசன உபகரணங்களுக்கு அரசு மானியங்களை வழங்கலாம் அல்லது கிராமப்புறங்களில் நீர்ப்பாசன வசதிகளை மேம்படுத்த தனியார் நிறுவனங்களுடன் பங்குதாரர் ஆகலாம்',
               'கிசான் கிரெடிட் கார்டு திட்டம்: இந்தத் திட்டம் விவசாயிகளுக்கு அவர்களின் விவசாயம் மற்றும் பிற தொடர்புடைய நிதித் தேவைகளைப் பூர்த்தி செய்வதற்காக குறைந்த வட்டி விகிதத்தில் குறுகிய கால கடனுக்கான அணுகலை வழங்குகிறது',
               'விலை நிலைப்படுத்தல் நடவடிக்கைகள்: சந்தையில் ஏற்ற இறக்கத்தால் விளைந்த பயிர்களுக்கு உரிய விலை கிடைக்காமல் விவசாயிகள் அடிக்கடி போராடி வருகின்றனர். குறைந்தபட்ச ஆதரவு விலைகள் போன்ற விலை நிலைப்படுத்தல் நடவடிக்கைகளை நடைமுறைப்படுத்துவது விவசாயிகளுக்கு நிலையான வருமானத்தை வழங்குவதோடு அவர்களின் நிதி அபாயத்தையும் குறைக்கும்',
               'பிரதான் மந்திரி க்ரிஷி சிஞ்சாய் யோஜனா: பாசன வசதிகளை வழங்குதல், திறமையான நீர் பயன்பாட்டை ஊக்குவித்தல் மற்றும் கிராமப்புறங்களில் நீர் பாதுகாப்பு உள்கட்டமைப்பை மேம்படுத்துதல் ஆகியவற்றின் மூலம் பண்ணை உற்பத்தியை மேம்படுத்துவதை இந்த திட்டம் நோக்கமாகக் கொண்டுள்ளது']

    if(lang=='tamil'):
        print(tam_sol)
    elif(lang=='english'):
        print(eng_sol)
    else:
        print(hin_sol)

def flood():
    eng_sol = ['Crop insurance: Farmers can purchase crop insurance to protect against crop losses due to floods. This can provide them with financial support to cover their losses and help them recover from the impact of floods.',
               'Farmers can grow flood-resistant crops such as rice, which can survive in waterlogged conditions. The government can provide support in terms of subsidies and technical assistance to promote the cultivation of such crops',
               'Farmers can take steps to protect their livestock during floods, such as moving them to higher ground, providing them with food and shelter, and ensuring their safety during evacuation']

    hin_sol = ['फसल बीमा: बाढ़ के कारण फसल के नुकसान से बचाने के लिए किसान फसल बीमा खरीद सकते हैं। यह उन्हें अपने नुकसान को कवर करने के लिए वित्तीय सहायता प्रदान कर सकता है और उन्हें बाढ़ के प्रभाव से उबरने में मदद कर सकता है।',
               'किसान चावल जैसी बाढ़ प्रतिरोधी फसलें उगा सकते हैं, जो जलभराव की स्थिति में जीवित रह सकती हैं। सरकार ऐसी फसलों की खेती को बढ़ावा देने के लिए सब्सिडी और तकनीकी सहायता के रूप में सहायता प्रदान कर सकती है',
               'किसान बाढ़ के दौरान अपने पशुओं की सुरक्षा के लिए कदम उठा सकते हैं, जैसे कि उन्हें ऊंची जमीन पर ले जाना, उन्हें भोजन और आश्रय प्रदान करना और निकासी के दौरान उनकी सुरक्षा सुनिश्चित करना']
    
    tam_sol = ['பயிர்க் காப்பீடு: வெள்ளத்தால் ஏற்படும் பயிர் இழப்புகளிலிருந்து பாதுகாக்க விவசாயிகள் பயிர்க் காப்பீட்டை வாங்கலாம். இதன் மூலம் அவர்களுக்கு ஏற்படும் இழப்பை ஈடுகட்ட நிதியுதவி வழங்குவதுடன் வெள்ள பாதிப்பில் இருந்து மீளவும் முடியும்.',
               'விவசாயிகள் நெல் போன்ற வெள்ளத்தை எதிர்க்கும் பயிர்களை பயிரிடலாம், இது தண்ணீர் தேங்கும் சூழ்நிலையிலும் வாழலாம். அத்தகைய பயிர்களின் சாகுபடியை ஊக்குவிக்க அரசு மானியங்கள் மற்றும் தொழில்நுட்ப உதவிகளின் அடிப்படையில் ஆதரவை வழங்க முடியும்',
               'வெள்ளத்தின் போது விவசாயிகள் தங்கள் கால்நடைகளை பாதுகாக்க நடவடிக்கை எடுக்கலாம்.']

    if(lang=='tamil'):
        print(tam_sol)
    elif(lang=='english'):
        print(eng_sol)
    else:
        print(hin_sol)


def chatgpt(query):
    payload = {
    "model": "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": query}],
    "n" : 1,
    "stream": False,
    "presence_penalty":0,
    "frequency_penalty":0,
    }

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai.api_key}"
    }

    try:
        response = requests.post(URL, headers=headers, json=payload, stream=False)
        result=json.loads(response.content.decode('utf-8'))
        final_result=(result['choices'][0]['message']['content'])
        print(final_result)
    
    except Exception as e:
        if(lang=='english'):
            print("We couldn't find any solution for the query")
        elif(lang=='hindi'):
            print('हमें इस प्रश्न का कोई हल नहीं मिला')
        else:
            print('இந்தக் கேள்விக்கு எங்களால் எந்த தீர்வையும் கண்டுபிடிக்க முடியவில்லை')



def beggining():
    global lang
    lang='english' # default
    wishMe()
    while (True):
        query = input().lower()
        if('drought' in query or 'water adequate' in query or 'water shortage' in query or 'dry' in query or('rain' in query and ('less' in query or 'low' in query)) or 'வறட்சி' in query or 'உலர்' in query or 'நீர் பற்றாக்குறை' in query or('water' in query and 'short' in query) or 'सूखा' in query or 'पानी की कमी' in query):
            drought()
        
        elif('fertility' in query or 'soil erosion' in query or 'मृदा अपरदन' in query or 'उपजाऊपन' in query or 'கருவுறுதல்' in query or 'மண்ணரிப்பு' in query):
            fertility()

        elif('poor' in query or 'capital' in query or 'money' in query or 'amount'in query or 'fund' in query or 'finance' in query or 'income' in query or 'संपत्ति' in query or 'धन' in query or 'गरीब' in query or 'पैसे' in query or 'रूपय' in query or 'कंगल' in query or 'कंगाल' in query or 'ஏழை' in query or 'சில்லறைகள்' in query or 'கங்கல்ரூபாய' in query or 'சொத்து' in query):
            money()

        elif('flood' in query or (('heavy' in query or 'high' in query) and 'rain' in query) or ('water' in query and 'overflow' in query) or 'बाढ़' in query or 'बाढ' in query or (('भारी' in query or 'तेज' in query or 'ज्यादा' in query) and 'वर्षा' in query) or 'வெள்ளம்' in query or 'கன மழை' in query or 'கடும் மழை' in query):
            flood()
        elif('ஹிந்தி' in query or 'hindi' in query):
            lang='hindi'
            # Change the input and output as hindi
            print('अब अब भाषा हिंदी में है')

        elif('tamil' in query or 'तमिल' in query):
            lang='tamil'
            # Change the input and output as tamil
            print('இப்போது இப்போது மொழி இந்தியில் உள்ளது')
        elif('अंग्रेजी' in query or 'इंग्लिश' in query or 'ஆங்கிலம்' in query):
            lang='english'
            # Change the input and output as english
            print('now now the language is in english')
        else:
            chatgpt(query)

beggining()




