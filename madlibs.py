ing_verb =input("Enter a verb ending in -ing: ")
adjective =input("Enter an adjective: ")
verb = input("Enter a verb: ")
verb2 = input("Enter a verb: ")
noun = input("Enter a noun: ")
plural_noun =  input("Enter a noun: ")
ing_verb2 =input("Enter a verb ending in -ing: ")
number =input("Enter a number: ")
plural_noun2 =  input("Enter a noun: ")

story = ("Football is fun when you are"
 + ing_verb + "with your" +adjective + 
 "teammates! The practices are difficult when coaches tell you to" 
 + verb + "the sled. If you get in trouble the coaches will make you" 
 +verb2 + ". The next game you play, you are facing" +noun+
 "Highschool. Some of their kids are as big as" +plural_noun+ 
 ". Your team isn’t worried though because all week you have been"
 +ing_verb2+ ". On Friday, you beat the other team" +number +
 " - 0. Coach congratulates the team and buys them all" +plural_noun2+ ".")
   
ready = input("Are you ready to see your story? ")

print(story)
if ready == "n":
   print("ok")
else:
   print(story)
   
wait =input(" ")
