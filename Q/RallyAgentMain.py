import RallyContext
import RallyAnalysis
import JasonSendMail






#MAIN

#Pull Orcavengers data from Rally using Rally API key
print "Get Rally Project Info"
r = RallyContext.RallyContext('apikey goes here')



#Analyse Rally data
print "Analyse"
analyses = [RallyAnalysis.rally_analysis_grooming_health(),
            RallyAnalysis.rally_analysis_wip()]

body = ''
for analysis in analyses:
    analysis.analyse(r)
    advice = analysis.print_advice()
    print advice
    body += advice + '\n'






