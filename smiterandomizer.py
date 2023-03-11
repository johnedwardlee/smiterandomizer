import random
import time
t = int( time.time() * 1000.0 )
random.seed( ((t & 0xff000000) >> 24) +
             ((t & 0x00ff0000) >>  8) +
             ((t & 0x0000ff00) <<  8) +
             ((t & 0x000000ff) << 24)   )

team1 = ['mid','solo','carry','jg','supp']
team2 = ['mid','solo','carry','jg','supp']
assassins = {'\tawilix' ,'\tbaka' ,'\tcama' ,'\tcat' ,'\tcleo' ,'\tda ji' ,'\tderg' ,'\thun batz' ,'\tkali' ,'\tlancelot' ,'\tloki' ,'\tmerc' ,'\tne zha' ,'\tnem' ,'\tpele' ,'\trat' ,'\trav' ,'\tserqet' ,'\tset' ,'\tspider' ,'\tsus' ,'\tthan' ,'\tthor' ,'\ttsuki' }
guardians = {'\tares' ,'\tathena' ,'\tatlas' ,'\tbear' ,'\tcab' ,'\tcerb' ,'\tcthulu' ,'\tdrunk' ,'\tfafnir' ,'\tganesha' ,'\tgeb' ,'\tjorm' ,'\tkhepri' ,'\tkumbha' ,'\tkuz' ,'\tmaui' ,'\tsobek' ,'\tsylv' ,'\tterra' ,'\txing' ,'\tyemoja' ,'\tymir' }
hunters = {'\tamc' ,'\tapollo' ,'\tartemis' ,'\tcern' ,'\tcharibdis' ,'\tchern' ,'\tchiron' ,'\tcupid' ,'\tdanza' ,'\thachi' ,'\theim' ,'\thou yi' ,'\tishtar' ,'\tiza' ,'\tjing' ,'\tlion' ,'\tmarti' ,'\tmedusa' ,'\tneith' ,'\trama' ,'\tskadi' ,'\tullr' ,'\txbal' }
mages = {'\tagni' ,'\tanubis' ,'\tao' ,'\taphro' ,'\tbaron' ,'\tbird nips' ,'\tchange' ,'\tchronos' ,'\tdisco' ,'\teset' ,'\tfreya' ,'\thades' ,'\thag' ,'\thebo' ,'\thel' ,'\thera' ,'\tjanus' ,'\tkui' ,'\tkuku' ,'\tmerlin' ,'\tmorgan' ,'\tmorrigan' ,'\tnox' ,'\tnu wa' ,'\tnuggets' ,'\tolorun' ,'\tpers' ,'\tpos' ,'\tpuch' ,'\tra' ,'\traijin' ,'\tscylla' ,'\tsol' ,'\ttia' ,'\tvulcan' ,'\tzeus' }
warriors = {'\tKA' ,'\tachilles' ,'\tama' ,'\tbellona' ,'\tchaac' ,'\tchu chu' ,'\terlang' ,'\tgilga' ,'\tguan' ,'\therc' ,'\thorus' ,'\tmonke' ,'\tmulan' ,'\tnike' ,'\todin' ,'\tosiris' ,'\tshiva' ,'\tsuitor' ,'\ttyr' ,'\tvamana' }          

def smitRandom(input):
    
    rand_assassins = random.sample(list(assassins), 2)
    rand_mages = random.sample(list(mages), 2)
    rand_warriors = random.sample(list(warriors), 2)
    rand_guardians = random.sample(list(guardians), 2)
    rand_hunters = random.sample(list(hunters), 2)
    random.shuffle(team1)
    random.shuffle(team2)
    if input == 'teams':
        out = 'Team 1: ' + str(team1) + '\n' +  'Team 2: ' + str(team2) + '\n'
    if input == 'mage':
        out = 'Mages: ' + ''.join(rand_mages)
    if input == 'warrior':
        out = 'Warriors: ' + ''.join(rand_warriors)
    if input == 'guardian':
        out = 'Guardians: ' + ''.join(rand_guardians)
    if input == 'assassin':
        out = 'Assassins: ' + ''.join(rand_assassins)
    if input == 'hunter':
        out = 'Hunters: ' + ''.join(rand_hunters)
    if input == None:
        out = 'Please type an input to the randomizer'

    return out



# print(team1)
# print(team2)
# print('\t\tJohn\t\t\tTrip')
# print('---------------------------------------------------------')
# print('assassins:' + ''.join(rand_assassins))
# print('mages:    ' + ''.join(rand_mages))
# print('warriors: ' + ''.join(rand_warriors))
# print('guardians:' + ''.join(rand_guardians))
# print('hunters:  ' + ''.join(rand_hunters))




