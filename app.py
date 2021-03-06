from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import time

app = Flask(__name__)
status = {}  # Using status to store the number to ensure IsLoggedIn as well as "Main Page(first menu)" or "FAQ_page (second menu)"


# sample --> { number :  [ "menu"|"faq_menu" , "human_support"|"bot_support" ] }

@app.route("/", methods=["get", "post"])
def reply():
    text = request.form.get("Body")
    number = request.form.get("From")
    number = number.replace("whatsapp:", "")
    option = None
    res = MessagingResponse()
    print(status)

    if number not in status:
        menu1 = res.message("ð¤ "
                            "Hi! ð Thanks for contacting *SwasthVritta Health Solutions* ð "
                            "\nWhat can we do for you today...ð"
                            "\n\nYou can choose from one of the options below:"
                            "\n\n*Type*\n"
                            "\n 1ï¸â£To view our *Products*"
                            "\n 2ï¸â£To know your *Unique Body Type*"
                            "\n 3ï¸â£ *FAQs*"
                            "\n 4ï¸â£To *contact* us"

                            "\n\n ```Type '/bye' to exit Bot``` ")
        menu1.media("https://media-exp1.licdn.com/dms/image/C4E0BAQEZGVoTS6N5Yw/company-logo_200_200/0/1637908454698?e"
                    "=2159024400&v=beta&t=QqFIOpiv9L6ltT23JAgsy8b6YrvOQa5w6XNeN52fUOI")
        status[number] = ["main", False]
        return str(res)

    if text.strip().lower() == "/bye":
        status.pop(number)
        res.message("Thank you for using for the chatbot"
                    "\nHave a good day ðð ")
        return str(res)

    if text.strip().upper() == "YES" and status[number][1] == "human_support":
        res.message("ð¤ \nPlease wait while I connect you to a human")
        res.message("ð¤ \nWe are away right at the moment, our team is currently operating at limited capacity,"
                    "\nWe appreciate your patienceð")
        res.message("ð¤ \nPlease leave your question, our support team will get back to you as soon as possibleð¤")
        status[number] = ["main", "bot_support"]
        return str(res)

    if status[number][0] == "main":
        try:
            option = int(text)
        except:
            res.message("Please enter a valid response."
                        "\nType 0ï¸â£ to view the *Main Menu*")
            return str(res)

        if option == 0:
            menu2 = res.message("\nYou can choose from one of the options below:"
                                "\n\n*Type*\n"
                                "\n 1ï¸â£ To view our *Products* "
                                "\n 2ï¸â£ To know your *Unique Body Type* "
                                "\n 3ï¸â£ *FAQs* "
                                "\n 4ï¸â£ To *contact* us"

                                "\n\n ```Type '/bye' to exit Bot``` "
                                )
            # menu2.media("https://drive.google.com/uc?export=view&id=10zRBV7yzDlNoOZN6vbyk578IRxDZKwnQ")
            status[number] = ["main", "bot_support"]
        elif option == 1:
            res.message(
                "We currently serve the following items: \n\nâ CHASS  \nâ DIPS \nâ SAUCES \nâ CHUTNEY \n"
                "\n Here are the details")
            p1 = res.message(
                "\nCHASS ð¥"
                "\n\n_â¹29.00-â¹39.00_"
                "\n_Benefits:_"
                "\n_Helpful in 50+ diseases_")
            p1.media("https://drive.google.com/uc?export=view&id=1QRsuh6IPdaTKzV66n86sWVn2VTUWNnLe")

            p2 = res.message("DIPS \n"
                             "\n"
                             "â¹399.00-â¹599.00\n"
                             "\n"
                             "Dips Ingredients:\n"
                             "- _Avocado_ \n"
                             "- _Tomato_ \n"
                             "- _Lemon juice_ \n"
                             "- _Hing_ \n"
                             "- _Pinch salt/pepper_ \n"
                             "- _+Many other herbs_ \n"
                             "\n"
                             "Paesley Dip Ingredients:\n"
                             "- _Ground Pine nuts_ \n"
                             "- _Dried parsley_ \n"
                             "- _Cider Vinegar_ \n"
                             "- _Honey_ \n"
                             "- _Udo's Oil_ \n"
                             "- _Hing_ \n"
                             "- _Cream_ \n"
                             "- _+Many other herbs_")
            p2.media("https://drive.google.com/uc?export=view&id=1OA5PmPLGh6HBdJ8tdZaCyf1iqn9-s9nf")

            p3 = res.message("Sauces \n\n"
                             "â¹399.00-â¹599.00\n"
                             "\n"
                             "Coriander Sauce Ingredients : \n"
                             "- _fresh coriander_ \n"
                             "- _fresh basil_ \n"
                             "- _fresh ginger_ \n"
                             "- _asparagus_ \n"
                             "- _spears_ \n"
                             "- _warm soya_ \n"
                             "- _milk_ \n"
                             "- _salt/pepper_ \n"
                             "- _+Many other Herbs_ \n"
                             "\n"
                             "Asparagus Sauce Ingredients : \n"
                             "- _Courgette_ \n"
                             "- _Asparagus_ \n"
                             "- _Coriander_ \n"
                             "- _Salt/Pepper_ \n"
                             "- _Bay Leaf_ \n"
                             "- _Cooked Lentils_ \n"
                             "- _+Many other Herbs_")
            p3.media("https://drive.google.com/uc?export=view&id=17ZFffRhZd774a3PlDv1mpC3sDqxwcY96")

            p4 = res.message("Chutney \n"
                             "\n"
                             "â¹299.00-â¹499.00\n"
                             "\n"
                             "Fresh Green Chutney Ingredients :\n"
                             "- _Parsley/coriander_\n"
                             "- _Lemon_\n"
                             "- _Cayenne pepper_\n"
                             "- _Almonds_\n"
                             "- _Water_\n"
                             "- _Salt to taste_\n"
                             "- _+Many other herbs_\n"
                             "\n"
                             "Dates & Pear Chutney Ingredients :\n"
                             "- _Pear_ \n"
                             "- _Dates_ \n"
                             "- _Paprika_ \n"
                             "- _Parsley_ \n"
                             "- _Ginger_ \n"
                             "- _French Mustard_ \n"
                             "- _+Many other herbs_")
            p4.media("https://drive.google.com/uc?export=view&id=1feosHca2-jtbe3MgVjG85ojjJK_xfmuW")
            status[number] = ["main", "bot_support"]

        elif option == 2:
            res.message("Please visit our _Prakriti Assessment_ link for assessing your 'Unique Body Type'\n"
                        "https://prakriti-assessment.stackblitz.io")
            status[number] = ["main", "bot_support"]

        elif option == 3:
            status[number][0] = "faq_menu"
            res.message("FAQ Menu\n\n"
                        "Type"
                        "\n1ï¸â£ Are your Products Safe?"
                        "\n2ï¸â£ Return Policies"
                        "\n3ï¸â£ Discounts"
                        "\n4ï¸â£ What are our working hours?"
                        "\n\n Type 0ï¸â£ to go back to *Main Menu*")

        elif option == 4:
            res.message("At SwasthVritta ð\n- We are availing our users the platform where they can consult with "
                        "Ayurveda Doctors and Health Advisors in 18 different Specialties through both Online and "
                        "Offline modes ð.")
            res.message('Contact SwasthVritta on \n+91 8160498700.'
                        '\n\nFollow Swasthvritta on Instagram \nhttps://www.instagram.com/swasthvritta to get recent updates.'
                        '\n\nAccess our official website \nhttps://www.swasthvritta.com for more services.'
                        '\n\nAnd do not forget to follow us on Linkedin \nhttps://in.linkedin.com/company/swasthvritta-health-solutions .'
                        '\n\nMail us at swasthvrittahealthsolutions@gmail.com.')
            res.message("Is your query resolved?"
                        "\nDo you want us to connect you to our customer support agent ð¨ or ð©?"
                        "\nIf so, please type YES.")
            status[number][1] = "human_support"
        else:
            res.message("Please enter a valid response"
                        "\nType 0ï¸â£ to view the *Main Menu*")

    elif status[number][0] == "faq_menu":

        try:
            option = int(text)
        except:
            res.message("Please enter a valid response."
                        "\nType 0ï¸â£ to go back to *Main Menu*")
            return str(res)

        if option == 0:
            menu3 = res.message("\nYou can choose from one of the options below:"
                                "\n\n*Type*\n"
                                "\n 1ï¸â£ To view our *Products* "
                                "\n 2ï¸â£ To know your *Unique Body Type* "
                                "\n 3ï¸â£ *FAQs* "
                                "\n 4ï¸â£ To *contact* us"

                                "\n\n ```Type '/bye' to exit Bot``` ")
            # menu3.media("https://drive.google.com/uc?export=view&id=10zRBV7yzDlNoOZN6vbyk578IRxDZKwnQ")
            status[number] = ["main", "bot_support"]
        elif option == 1:
            res.message(
                "All products served in *'SwasthVritta Health Solutions'* are Food Safety and Standards Authority of "
                "India ( _fssai_ ) authorised.ð "
                "\n\nThe products are very healthy and proven to give positive results.ð ")
        elif option == 2:
            res.message("All items purchased at SwasthVritta can be returned within 14 weekdays. "
                        "\nYou can read our return policy on the official website. ")
        elif option == 3:
            res.message(
                "Unfortunately, we currently donât provide any discount except for what you see on our website. ")
        elif option == 4:
            res.message("We currently operate from 9 a.m. to 6 p.m. "
                        "Go to 'Main Menu' to know our contacts details.")
        else:
            res.message("Please enter a valid response"
                        "\nType 0ï¸â£ to go back to *Main Menu*")
    return str(res)


if __name__ == "__main__":
    app.run()
