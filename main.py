import asyncio
import datetime
import aiohttp
import aiodns
from utils_1 import api_url as urls
import json
import time


binance_get_stock_price_url = urls.binance_get_stock_price_url
sym_list = ["1INCHUSDT",
            "1INCHBTC","1INCHUSDT","AAVEBTC","AAVEUSDT","ACAUSDT",]
            # "ACEUSDT","ACHUSDT","ACMUSDT","ADABTC","ADAETH","ADAFDUSD","ADAUSDC",
            # "ADAUSDT","ADXUSDT","AERGOUSDT","AEURUSDT","AEVOUSDT","AGIXBTC","AGIXUSDT",
            # "AGLDBTC","AGLDUSDT","AIUSDT","AKROUSDT","ALCXUSDT","ALGOBTC","ALGOUSDT",
            # "ALICEUSDT","ALPACABTC","ALPACAUSDT","ALPHABTC","ALPHAUSDT","ALPINEUSDT",
            # "ALTUSDC","ALTUSDT","AMBUSDT","AMPUSDT","ANKRBTC","ANKRUSDT","APEBTC","APEETH",
            # "APEUSDT","API3USDT","APTUSDT","ARBBTC","ARBFDUSD","ARBTC","ARBTUSD","ARBUSDC",
            # "ARBUSDT","ARDRUSDT","ARKMTUSD","ARKMUSDT","ARKUSDT","ARPABTC","ARPAUSDT","ARUSDT",
            # "ASRUSDT","ASTRUSDT","ASTUSDT","ATABTC","ATAUSDT","ATMUSDT","ATOMBTC","ATOMETH","ATOMFDUSD",
            # "ATOMUSDT","AUCTIONBTC","AUCTIONUSDT","AUDIOBTC","AUDIOUSDT","AVABTC","AVAUSDT","AVAXBTC","AVAXETH",
            # "AVAXFDUSD","AVAXUSDC","AVAXUSDT","AXLUSDT","AXSBTC","AXSUSDT","BADGERBTC","BADGERUSDT","BAKEBTC","BAKEUSDT",
            # "BALUSDT","BANDBTC","BANDUSDT","BARUSDT","BATBTC","BATUSDT","BBUSDT","BCHBTC","BCHFDUSD","BCHUSDC","BCHUSDT",
            # "BEAMXUSDT","BELBTC","BELUSDT","BETAUSDT","BICOBTC","BICOUSDT","BLURUSDT","BLZBTC","BLZUSDT","BNBBTC","BNBETH",
            # "BNBFDUSD","BNBTUSD","BNBUSDC","BNBUSDT","BNTBTC","BNTUSDT","BNXUSDT","BOMEFDUSD","BOMEUSDC","BOMEUSDT","BONDUSDT",
            # "BONKUSDC","BONKUSDT","BSWUSDT","BTCDAI","BTCFDUSD","BTCTUSD","BTCUSDC","BTCUSDT","BTTCUSDT","BURGERUSDT","C98BTC",
            # "C98USDT","CAKEBTC","CAKEUSDT","CELOBTC","CELOUSDT","CELRBTC","CELRUSDT","CFXBTC","CFXUSDT","CHESSUSDT","CHRBTC","CHRUSDT",
            # "CHZBTC","CHZFDUSD","CHZUSDT","CITYUSDT","CKBUSDT","CLVBTC","CLVUSDT","COMBOUSDT","COMPBTC","COMPUSDT","COSUSDT","COTIBTC",
            # "COTIUSDT","CREAMUSDT","CRVBTC","CRVUSDT","CTKBTC","CTKUSDT","CTSIBTC","CTSIUSDT","CTXCBTC","CTXCUSDT","CVCUSDT","CVPUSDT",
            # "CVXUSDT","CYBERUSDT","DARBTC","DARUSDT","DASHBTC","DASHUSDT","DATABTC","DATAUSDT","DCRUSDT","DEGOUSDT","DENTUSDT","DEXEUSDT",
            # "DFUSDT","DGBBTC","DGBUSDT","DIABTC","DIAUSDT","DOCKBTC","DOCKUSDT","DODOBTC","DODOUSDT","DOGEBTC","DOGEFDUSD","DOGEUSDC","DOGEUSDT",
            # "DOTBTC","DOTFDUSD","DOTUSDC","DOTUSDT","DUSKBTC","DUSKUSDT","DYDXBTC","DYDXFDUSD","DYDXUSDT","DYMUSDT","EDUUSDT","EGLDBTC","EGLDUSDT",
            # "ELFBTC","ELFUSDT","ENABTC","ENAFDUSD","ENAUSDC","ENAUSDT","ENJBTC","ENJUSDT","ENSBTC","ENSUSDT","EOSBTC","EOSUSDT","EPXUSDT","ERNUSDT",
            # "ETCBTC","ETCFDUSD","ETCUSDT","ETHBTC","ETHDAI","ETHFDUSD","ETHFIUSDT","ETHTUSD","ETHUSDC","ETHUSDT","FARMUSDT","FDUSDUSDT","FETBTC","FETUSDT",
            # "FIDAUSDT","FILBTC","FILFDUSD","FILUSDC","FILUSDT","FIOUSDT","FIROUSDT","FISBTC","FISUSDT","FLMBTC","FLMUSDT","FLOKIUSDT","FLOWBTC","FLOWUSDT","FLUXBTC",
            # "FLUXUSDT","FORTHUSDT","FORUSDT","FRONTBTC","FRONTUSDT","FTMBTC","FTMETH","FTMFDUSD","FTMUSDT","FTTUSDT","FUNUSDT","FXSUSDT","GALABTC","GALAFDUSD","GALAUSDT","GALUSDT","GASBTC","GASUSDT","GFTUSDT","GHSTUSDT","GLMBTC","GLMRUSDT","GLMUSDT","GMTUSDT","GMXUSDT","GNOUSDT","GNSUSDT","GRTBTC","GRTETH","GRTUSDT","GTCBTC","GTCUSDT","HARDUSDT","HBARBTC","HBARUSDT","HFTUSDT","HIFIUSDT","HIGHBTC","HIGHUSDT","HIVEBTC","HIVEUSDT","HOOKUSDT","HOTUSDT","ICPBTC","ICPUSDT","ICXBTC","ICXUSDT","IDBTC","IDEXBTC","IDEXUSDT","IDUSDT","ILVBTC","ILVUSDT","IMXUSDT","INJBTC","INJFDUSD","INJUSDC","INJUSDT","IOSTUSDT","IOTABTC","IOTAUSDT","IOTXBTC","IOTXETH","IOTXUSDT","IQUSDT","IRISUSDT","JASMYUSDT","JOEUSDT","JSTBTC","JSTUSDT","JTOUSDT","JUPUSDT","JUVUSDT","KAVABTC","KAVAUSDT","KDAUSDT","KEYUSDT","KLAYUSDT","KMDBTC","KMDUSDT","KNCBTC","KNCUSDT","KP3RUSDT","KSMBTC","KSMUSDT","LAZIOUSDT","LDOFDUSD","LDOUSDT","LEVERUSDT","LINABTC","LINAUSDT","LINKBTC","LINKETH","LINKFDUSD","LINKUSDC","LINKUSDT","LITBTC","LITUSDT","LOKAUSDT","LOOMBTC","LOOMUSDT","LPTBTC","LPTUSDT","LQTYUSDT","LRCBTC","LRCUSDT","LSKBTC","LSKUSDT","LTCBTC","LTCETH","LTCFDUSD","LTCUSDC","LTCUSDT","LTOBTC","LTOUSDT","LUNAUSDT","LUNCUSDT","MAGICUSDT","MANABTC","MANAUSDT","MANTAUSDT","MASKUSDT","MATICBTC","MATICFDUSD","MATICUSDC","MATICUSDT","MAVUSDT","MBLUSDT","MBOXBTC","MBOXUSDT","MDTBTC","MDTUSDT","MDXBTC","MDXUSDT","MEMEUSDT","METISUSDT","MINABTC","MINAUSDT","MKRBTC","MKRUSDT","MLNUSDT","MOVRBTC","MOVRUSDT","MTLBTC","MTLUSDT","NEARBTC","NEARFDUSD","NEARUSDC","NEARUSDT","NEOBTC","NEOUSDC","NEOUSDT","NEXOUSDT","NFPUSDT","NKNBTC","NKNUSDT","NMRBTC","NMRUSDT","NTRNUSDT","NULSBTC","NULSUSDT","OAXUSDT","OCEANBTC","OCEANUSDT","OGNBTC","OGNUSDT","OGUSDT","OMBTC","OMGUSDT","OMNIUSDT","OMUSDT","ONEBTC","ONEUSDT","ONGBTC","ONGUSDT","ONTBTC","ONTUSDT","OOKIUSDT","OPBTC","OPFDUSD","OPUSDC","OPUSDT","ORDIFDUSD","ORDIUSDC","ORDIUSDT","ORNUSDT","OSMOUSDT","OXTBTC","OXTUSDT","PAXGBTC","PAXGUSDT","PDAUSDT","PENDLEUSDC","PENDLEUSDT","PEOPLEBTC","PEOPLEUSDT","PEPEFDUSD","PEPETUSD","PEPEUSDC","PEPEUSDT","PERPBTC","PERPUSDT","PHAUSDT","PHBUSDT","PIVXUSDT","PIXELUSDT","POLSUSDT","POLYXUSDT","PONDBTC","PONDUSDT","PORTALUSDT","PORTOUSDT","POWRBTC","POWRUSDT","PROMUSDT","PROSUSDT","PSGUSDT","PUNDIXUSDT","PYRBTC","PYRUSDT","PYTHUSDT","QIUSDT","QKCUSDT","QNTBTC","QNTUSDT","QTUMBTC","QTUMUSDT","QUICKUSDT","RADBTC","RADUSDT","RAREBTC","RAREUSDT","RAYUSDT","RDNTUSDT","REEFUSDT","REIUSDT","RENBTC","RENUSDT","REQBTC","REQUSDT","REZUSDT","RIFUSDT","RLCBTC","RLCUSDT","RNDRBTC","RNDRUSDT","RONINUSDT","ROSEBTC","ROSEUSDT","RPLUSDT","RSRUSDT","RUNEBTC","RUNEUSDT","RVNBTC","RVNUSDT","SAGABTC","SAGAFDUSD","SAGAUSDT","SANDBTC","SANDUSDT","SANTOSUSDT","SCRTUSDT","SCUSDT","SEIBTC","SEIFDUSD","SEITUSD","SEIUSDT","SFPBTC","SFPUSDT","SHIBDOGE","SHIBFDUSD","SHIBUSDC","SHIBUSDT","SKLBTC","SKLUSDT","SLPETH","SLPUSDT","SNTUSDT","SNXBTC","SNXUSDT","SOLBTC","SOLETH","SOLFDUSD","SOLUSDC","SOLUSDT","SPELLUSDT","SSVUSDT","STEEMUSDT","STGUSDT","STMXUSDT","STORJBTC","STORJUSDT","STPTBTC","STPTUSDT","STRAXUSDT","STRKUSDT","STXBTC","STXUSDT","SUIBTC","SUIFDUSD","SUITUSD","SUIUSDC","SUIUSDT","SUNUSDT","SUPERBTC","SUPERUSDT","SUSHIBTC","SUSHIUSDT","SXPBTC","SXPUSDT","SYNUSDT","SYSBTC","SYSUSDT","TAOUSDT","TFUELBTC","TFUELUSDT","THETABTC","THETAUSDT","TIAFDUSD","TIAUSDC","TIAUSDT","TKOBTC","TKOUSDT","TLMBTC","TLMUSDT","TNSRUSDT","TRBBTC","TRBUSDT","TROYUSDT","TRUBTC","TRUUSDT","TRXBTC","TRXETH","TRXUSDT","TUSDT","TUSDUSDT","TWTUSDT","UFTUSDT","UMABTC","UMAUSDT","UNFIBTC","UNFIUSDT","UNIBTC","UNIUSDT","USDCUSDT","USDPUSDT","USDTDAI","USTCUSDT","UTKBTC","UTKUSDT","VANRYUSDT","VETBTC","VETETH","VETUSDT","VIBUSDT","VICUSDT","VIDTUSDT","VITEUSDT","VOXELBTC","VOXELUSDT","VTHOUSDT","WANBTC","WANUSDT","WAVESBTC","WAVESUSDT","WAXPBTC","WAXPUSDT","WBETHETH","WBETHUSDT","WIFUSDC","WIFUSDT","WINGUSDT","WINUSDT","WLDBTC","WLDFDUSD","WLDUSDC","WLDUSDT","WNXMUSDT","WOOUSDT","WRXUSDT","WUSDT","XAIFDUSD","XAIUSDT","XECUSDT","XEMUSDT","XLMBTC",
            # "XLMUSDT","XNOUSDT","XRPBTC","XRPETH","XRPFDUSD","XRPUSDC","XRPUSDT","XTZBTC","XTZUSDT","XVGUSDT","XVSBTC","XVSUSDT","YFIBTC","YFIUSDT","YGGBTC","YGGUSDT","ZECBTC","ZECUSDT","ZENUSDT","ZILBTC","ZILUSDT","ZRXBTC","ZRXUSDT",]


result = {}
async def worker(name, queue):
    while True:
        # Get a "work item" out of the queue.
       
        queue_item = await queue.get()
        rel = queue_item[0]
        symbol = queue_item[1]

        # Sleep for the "sleep_for" seconds.
        # rel = await response.text()

        # Notify the queue that the "work item" has been processed.
        queue.task_done()
        print("size" , queue.qsize())
        symbol, sum_price = process_stock_data(rel, symbol)
        result[symbol] = sum_price        
        print(f'{name}')
        print('Time: {}'.format(datetime.datetime.now()))


        
async def request_api(session, symbol):
    async with session.get(binance_get_stock_price_url.format(symbol)) as response:
        # await asyncio.sleep(1)
        print('Time: {}'.format(datetime.datetime.now()))
        rel = await response.text()
        return rel, symbol



def process_stock_data(rel, symbol):
    json_rel = json.loads(rel)
    close_price = list((float((json_rel[i][4])) for i in range(0, len(json_rel))))
    sum_price = float(sum(close_price))
    print("{}:".format(symbol), sum_price)
    return symbol, sum_price



def get_ten_stock_codes(result):    
    code_price = list(dict(sorted(result.items(), key=lambda item: item[1])).keys())
    print(code_price[-10:])
    final_list = code_price[-10:]
    return final_list

            
async def run():
    queue = asyncio.Queue(maxsize=5)
    async with aiohttp.ClientSession() as session: 
        requests = [
            asyncio.create_task(request_api(session, symbol)) for symbol in sym_list
        ]

   
        for req in requests:
            rel, symbol = await req
            await queue.put([rel, symbol])

        
    print('pass')
    tasks = []
    for i in range(3):
        task = asyncio.create_task(worker(f'worker-{i}', queue))
        tasks.append(task)   
    print("size_first" , queue.qsize())
        
    #wait ultil the queue has been processed completely
    start_time = time.monotonic()
    await queue.join()
    end_time = time.monotonic() - start_time
    print('end_time: ', end_time)

    # Cancel our worker tasks.
    for task in tasks:
        task.cancel()
    # Wait until all worker tasks are cancelled.
    await asyncio.gather(*tasks, return_exceptions=True)

    print("Top 10 codes: ", get_ten_stock_codes(result))
    print(result)

###
loop = asyncio.get_event_loop()
loop.run_until_complete(run())

# asyncio.run(run())