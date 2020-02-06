import matplotlib.pyplot as plt;

plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt

data = [('stowaways', 1.1305966680133086), ('evade', 1.1210532597613863), ('dacoits', 1.1154384397278359), ('captivity', 1.1114102015411096), ('robbers', 1.1063463328790002), ('inmates', 1.1061197745624145), ('smugglers', 1.1048513927529913), ('kidnappers', 1.1021755111045202), ('disembark', 1.1003376731407364), ('guards', 1.098983452322253), ('unscathed', 1.0972780809009044), ('surviving', 1.0957689082991882), ('octuplets', 1.0950900355178526), ('deserters', 1.0947983553448979), ('hostages', 1.0947897222845042), ('trusties', 1.0947675342745509), ('warders', 1.0947262537639542), ('shielded', 1.094315421710301), ('suspects', 1.0938153624038243), ('accomplices', 1.0935021345759872), ('traffickers', 1.093056561440489), ('lawmen', 1.0929301125992918), ('fraternizing', 1.0925549732816304), ('shoplifters', 1.0921073657548466), ('convicts', 1.0913389216578802), ('retract', 1.0910833882252937), ('drawstrings', 1.0905486971421794), ('destructible', 1.0890381057325766), ('pursuers', 1.0886089648052408), ('hijackers', 1.0884661639616722), ('prisoners', 1.0882039393370746), ('juveniles', 1.0881455182719841), ('captors', 1.087765728421083), ('captives', 1.0877185994293737), ('lookouts', 1.0865747365406921), ('contraband', 1.0863227658280021), ('runaways', 1.0862291053114437), ('deportees', 1.0849812363477023), ('unescorted', 1.0837233566377615), ('crewmen', 1.0834568062715408), ('remissions', 1.083107842983866), ('bodyguards', 1.0823856426087086), ('abductors', 1.0823179231200415), ('marksmen', 1.0819430397453789), ('occupants', 1.0808356509142434), ('shopkeepers', 1.0798124150881283), ('detainees', 1.0793611531681175), ('pickpockets', 1.0786598055145762), ('eyewitnesses', 1.0782516921615644), ('commandos', 1.0782338722228961), ('lifeboats', 1.0770543165925794), ('cower', 1.0762727890007262), ('dowries', 1.0762624630251372), ('jailers', 1.0758957754491845), ('lensman', 1.0758379816621266), ('cobras', 1.075675030252062), ('survive', 1.0755497535412837), ('undetected', 1.0754430738627068), ('shies', 1.0754019872574576), ('interrogators', 1.074566508964764), ('transgress', 1.0742976580821104), ('shackles', 1.0737245085122575), ('commandoes', 1.0731455134522652), ('prison', 1.0725674299303571), ('disembarking', 1.0722758574133222), ('alighting', 1.0721866820365344), ('cannibals', 1.0720910638210377), ('bystanders', 1.0717215931345885), ('jailors', 1.0712036872098527), ('moviemakers', 1.0711989904652208), ('illusionists', 1.071073833513675), ('escapers', 1.07061548027534), ('ransoms', 1.0704984646986753), ('extinguish', 1.0703573104466362), ('withstand', 1.0702188664511785), ('axons', 1.0702052327816496), ('penitentiary', 1.0699075624946428), ('underworld', 1.0697263755380648), ('bruises', 1.0694291466801968), ('prisoner', 1.0690618407367405), ('emerge', 1.0689582633437449), ('cellblock', 1.0687904921011293), ('custody', 1.068784378433984), ('hideout', 1.0686527280489646), ('assassins', 1.0681377645404355), ('dhows', 1.0679954205413558), ('gravest', 1.067933219145114), ('encounter', 1.0679306255924335), ('cellmates', 1.0679111870881237), ('ordeal', 1.0678985831454795), ('prisons', 1.0678211313868466), ('abductor', 1.0678049436818486), ('captor', 1.0677255847648144), ('noncombat', 1.067461633318891), ('bondsmen', 1.067323820684307), ('sharecropper', 1.067148427985045), ('bondsman', 1.0669339548483976), ('flashover', 1.0666019826359663), ('wartime', 1.066370295723617), ('handcuffs', 1.0659281240064373)]

objects = [x[0] for x in reversed(data[:30])]
y_pos = np.arange(len(objects))
performance = [x[1] for x in reversed(data[:30])]

plt.barh(y_pos, performance, align='center', alpha=0.5)

plt.yticks(y_pos, objects)
plt.xlabel('Rating')
plt.title('Spammiest Words')
plt.xlim(xmin=1, xmax=1.13)

plt.show()
