from flask import Flask, request

app = Flask(__name__)
status = {}  # Using status to store the number to ensure IsLoggedIn as well as "Main Page(first menu)" or "FAQ_page (second menu)"


# sample --> { number :  [ "menu"|"faq_menu" , "human_support"|"bot_support" ] }

@app.route("/", methods=["get", "post"])

def reply():
    text = request.form.get("message")
    number = request.form.get("sender")
    option = None
    res = {
        "reply": ""
    }
    print(status)
    if number not in status:
        menu1 = res["reply"] = res["reply"] + "\n" + "🤖\n Hi! 👋 Thanks for contacting *SwasthVritta Health Solutions* 💚" \
                                                     "\nWhat can we do for you today...🌟\n\nYou can choose from one of the options below:" \
                                                     "\n\n*Type*\n" + \
                               "\n 1️⃣To view our *Products*" + \
                               "\n 2️⃣To know your *Unique Body Type*" + \
                               "\n 3️⃣ *FAQs*" \
                               "\n 4️⃣To *contact* us" + \
                               "\n\n ```Type '/bye' to exit Bot``` "
        # menu1.media("https://media-exp1.licdn.com/dms/image/C4E0BAQEZGVoTS6N5Yw/company-logo_200_200/0/1637908454698?e=2159024400&v=beta&t=QqFIOpiv9L6ltT23JAgsy8b6YrvOQa5w6XNeN52fUOI")
        status[number] = ["main", False]
        return str(res)

    if text.strip().lower() == "/bye":
        status.pop(number)
        res["reply"] = res["reply"] + "\n" + "Thank you for using for the chatbot " \
                                             "\nHave a good day 😃🍀 "
        return str(res)

    if text.strip().upper() == "YES" and status[number][1] == "human_support":
        res["reply"] = res["reply"] + "\n" + "🤖 \nPlease wait while I connect you to a human"
        res["reply"] = res["reply"] + "\n" + "🤖 \nWe are away right at the moment, our team is currently operating at " \
                                             "limited capacity,\nWe appreciate your patience🙏"
        res["reply"] = res[
                           "reply"] + "\n" + "🤖 \nPlease leave your question, our support team will get back to you as soon as possible🤞"
        status[number] = ["main", "bot_support"]
        return str(res)

    if status[number][0] == "main":
        try:
            option = int(text)
        except:
            res["reply"] = res["reply"] + "\n" + "Please enter a valid response." \
                                                 "\nType 0️⃣ to view the *Main Menu*"
            return str(res)

        if option == 0:
            menu2 = res["reply"] = res["reply"] + "\n" + "\nYou can choose from one of the options below:" \
                                                         "\n\n*Type*\n" \
                                                         "\n 1️⃣ To view our *Products* " \
                                                         "\n 2️⃣ To know your *Unique Body Type* " \
                                                         "\n 3️⃣ *FAQs* " \
                                                         "\n 4️⃣ To *contact* us" \
                                                         "\n\n ```Type '/bye' to exit Bot``` "

            # menu2.media("https://drive.google.com/uc?export=view&id=10zRBV7yzDlNoOZN6vbyk578IRxDZKwnQ")
            status[number] = ["main", "bot_support"]
        elif option == 1:
            res["reply"] = res[
                               "reply"] + "\n" + "We currently serve the following items: \n\n✅ CHASS  \n✅ DIPS \n✅ SAUCES \n✅ CHUTNEY " \
                                                 "\n\n Here are the details"
            p1 = res["reply"] = res["reply"] + "\n" + \
                                "\nCHASS 🥛" \
                                "\n\n_₹29.00-₹39.00_" \
                                "\n_Benefits:_" \
                                "\n_Helpful in 50+ diseases_"
            # p1.media("https://drive.google.com/uc?export=view&id=1QRsuh6IPdaTKzV66n86sWVn2VTUWNnLe")

            p2 = res["reply"] = res["reply"] + "\n" + \
                                "DIPS \n" \
                                "\n" \
                                "₹399.00-₹599.00\n" \
                                "\n" \
                                "Dips Ingredients:\n" \
                                "- _Avocado_ \n" \
                                "- _Tomato_ \n" \
                                "- _Lemon juice_ \n" \
                                "- _Hing_ \n" \
                                "- _Pinch salt/pepper_ \n" \
                                "- _+Many other herbs_ \n" \
                                "\n" \
                                "Paesley Dip Ingredients:\n" \
                                "- _Ground Pine nuts_ \n" \
                                "- _Dried parsley_ \n" \
                                "- _Cider Vinegar_ \n" \
                                "- _Honey_ \n" \
                                "- _Udo's Oil_ \n" \
                                "- _Hing_ \n" \
                                "- _Cream_ \n" \
                                "- _+Many other herbs_"
            # p2.media("https://drive.google.com/uc?export=view&id=1OA5PmPLGh6HBdJ8tdZaCyf1iqn9-s9nf")

            p3 = res["reply"] = res["reply"] + "\n" + "Sauces \n\n" \
                                                      "₹399.00-₹599.00\n" \
                                                      "\n" \
                                                      "Coriander Sauce Ingredients : \n" \
                                                      "- _fresh coriander_ \n" \
                                                      "- _fresh basil_ \n" \
                                                      "- _fresh ginger_ \n" \
                                                      "- _asparagus_ \n" \
                                                      "- _spears_ \n" \
                                                      "- _warm soya_ \n" \
                                                      "- _milk_ \n" \
                                                      "- _salt/pepper_ \n" \
                                                      "- _+Many other Herbs_ \n" \
                                                      "\n" \
                                                      "Asparagus Sauce Ingredients : \n" \
                                                      "- _Courgette_ \n" \
                                                      "- _Asparagus_ \n" \
                                                      "- _Coriander_ \n" \
                                                      "- _Salt/Pepper_ \n" \
                                                      "- _Bay Leaf_ \n" \
                                                      "- _Cooked Lentils_ \n" \
                                                      "- _+Many other Herbs_"
            # p3.media("https://drive.google.com/uc?export=view&id=17ZFffRhZd774a3PlDv1mpC3sDqxwcY96")

            p4 = res["reply"] = res["reply"] + "\n" + "Chutney \n" \
                                                      "\n" \
                                                      "₹299.00-₹499.00\n" \
                                                      "\n" \
                                                      "Fresh Green Chutney Ingredients :\n" \
                                                      "- _Parsley/coriander_\n" \
                                                      "- _Lemon_\n" \
                                                      "- _Cayenne pepper_\n" \
                                                      "- _Almonds_\n" \
                                                      "- _Water_\n" \
                                                      "- _Salt to taste_\n" \
                                                      "- _+Many other herbs_\n" \
                                                      "\n" \
                                                      "Dates & Pear Chutney Ingredients :\n" \
                                                      "- _Pear_ \n" \
                                                      "- _Dates_ \n" \
                                                      "- _Paprika_ \n" \
                                                      "- _Parsley_ \n" \
                                                      "- _Ginger_ \n" \
                                                      "- _French Mustard_ \n" \
                                                      "- _+Many other herbs_"
            # p4.media("https://drive.google.com/uc?export=view&id=1feosHca2-jtbe3MgVjG85ojjJK_xfmuW")
            status[number] = ["main", "bot_support"]

        elif option == 2:
            res["reply"] = res[
                               "reply"] + "\n" + "Please visit our _Prakriti Assessment_ link for assessing your 'Unique Body " \
                                                 "Type'\n" \
                                                 "https://prakriti-assessment.stackblitz.io"
            status[number] = ["main", "bot_support"]

        elif option == 3:
            status[number][0] = "faq_menu"
            res["reply"] = res["reply"] + "\n" + "FAQ Menu\n\n" \
                                                 "Type" \
                                                 "\n1️⃣ Are your Products Safe?" \
                                                 "\n2️⃣ Return Policies" \
                                                 "\n3️⃣ Discounts" \
                                                 "\n4️⃣ What are our working hours?" \
                                                 "\n\n Type 0️⃣ to go back to *Main Menu*"
        elif option == 4:
            res["reply"] = res[
                               "reply"] + "\n" + "At SwasthVritta 💚\n- We are availing our users the platform where they can consult with " \
                                                 "Ayurveda Doctors and Health Advisors in 18 different Specialties through both Online and Offline modes 🌞."
            res["reply"] = res["reply"] + "\n" + 'Contact SwasthVritta on \n+91 8160498700.' \
                                                 '\n\nFollow Swasthvritta on Instagram \nhttps://www.instagram.com/swasthvritta to get recent updates.' \
                                                 '\n\nAccess our official website \nhttps://www.swasthvritta.com for more services.' \
                                                 '\n\nAnd do not forget to follow us on Linkedin \nhttps://in.linkedin.com/company/swasthvritta-health-solutions .' \
                                                 '\n\nMail us at swasthvrittahealthsolutions@gmail.com.'
            res["reply"] = res["reply"] + "\n" + "Is your query resolved?" \
                                                 "\nDo you want us to connect you to our customer support agent 👨 or 👩?" \
                                                 "\nIf so, please type YES."
            status[number][1] = "human_support"
        else:
            res["reply"] = res["reply"] + "\n" + "Please enter a valid response" \
                                                 "\nType 0️⃣ to view the *Main Menu*"

    elif status[number][0] == "faq_menu":

        try:
            option = int(text)
        except:
            res["reply"] = res["reply"] + "\n" + "Please enter a valid response." \
                                                 "\nType 0️⃣ to go back to *Main Menu*"
            return str(res)

        if option == 0:
            menu3 = res["reply"] = res["reply"] + "\n" + "\nYou can choose from one of the options below:" \
                                                         "\n\n*Type*\n" \
                                                         "\n 1️⃣ To view our *Products* " \
                                                         "\n 2️⃣ To know your *Unique Body Type* " \
                                                         "\n 3️⃣ *FAQs* " \
                                                         "\n 4️⃣ To *contact* us" \
                                                         "\n\n ```Type '/bye' to exit Bot``` "
            # menu3.media("https://drive.google.com/uc?export=view&id=10zRBV7yzDlNoOZN6vbyk578IRxDZKwnQ")
            status[number] = ["main", "bot_support"]
        elif option == 1:
            res["reply"] = res[
                               "reply"] + "\n" + "All products served in *'SwasthVritta Health Solutions'* are Food Safety " \
                                                 "and Standards Authority of India ( _fssai_ ) authorised.👌" \
                                                 "\n\nThe products are very healthy and proven to give positive results.😊 "
        elif option == 2:
            res["reply"] = res[
                               "reply"] + "\n" + "All items purchased at SwasthVritta can be returned within 14 weekdays. " \
                                                 "\nYou can read our return policy on the official website. "
        elif option == 3:
            res["reply"] = res[
                               "reply"] + "\n" + "Unfortunately, we currently don’t provide any discount except for what you " \
                                                 "see on our website. "
        elif option == 4:
            res["reply"] = res["reply"] + "\n" + "We currently operate from 9 a.m. to 6 p.m. " \
                                                 "Go to 'Main Menu' to know our contacts details."
        else:
            res["reply"] = res["reply"] + "\n" + "Please enter a valid response" \
                                                 "\nType 0️⃣ to go back to *Main Menu*"
    return str(res)


if __name__ == "__main__":
    app.run()
