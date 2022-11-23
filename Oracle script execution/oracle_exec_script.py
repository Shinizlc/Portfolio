##first option using subprocess
import subprocess as sp
from loguru import logger
import os
import csv
import cx_Oracle
from columnar import Columnar
os.environ['PATH']='/Users/aleksei.semerikov/OracleClient/instantclient_12_2:/Users/aleksei.semerikov/OracleClient/instantclient_12_2:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin:/Library/Frameworks/Mono.framework/Versions/Current/Commands'
os.environ['TNS_ADMIN']='/Users/aleksei.semerikov/OracleClient/instantclient_12_2/network'
os.environ['ORACLE_HOME']='/Users/aleksei.semerikov/OracleClient/instantclient_12_2'

list_of_db=['PRO-ADB011', 'PRO-ADB012','PRO-ADB021', 'PRO-ADB022','PRO-ADB031', 'PRO-ADB032','PRO-ADB041', 'PRO-ADB042','PRO-ADB051','PRO-ADB052',
'PRO-ADB061', 'PRO-ADB062','PRO-ADB071', 'PRO-ADB072','PRO-ADB081','PRO-ADB082','PRO-ADB101','PRO-ADB102','PRO-ADB111',
'PRO-ADB112','PRO-ADB121','PRO-ADB122','PRO-ADB131','PRO-ADB132','PRO-ADB141','PRO-ADB142','PRO-ADB151','PRO-ADB152','PRO-ADB161','PRO-ADB162',
'PRO-ADB171','PRO-ADB172','PRO-ADB201','PRO-ADB202','PRO-ADB211','PRO-ADB241','PRO-ADB242','PRO-ADB311','PRO-ADB312','PRO-ADB321',
'PRO-ADB322','PRO-ADB331','PRO-ADB332','PRO-ADB341','PRO-ADB342','PRO-ADB351','PRO-ADB352','PRO-ADB361','PRO-ADB362']
#
# list_of_db=['PRO-ADB311','PRO-ADB312','PRO-ADB321','PRO-ADB322','PRO-ADB331',
#             'PRO-ADB332','PRO-ADB341','PRO-ADB342','PRO-ADB351','PRO-ADB352','PRO-ADB361','PRO-ADB362']


# list_of_db=['PRO-ADB311']



# list_of_db=['OPS-STG-ADB011','OPS-STG-ADB012','OPS-STG-ADB021','OPS-STG-ADB022']

# with open('31-36pods.log', 'w') as file:
#     for db in list_of_db:
#     #why do we need the stdin=sp.PIPE even if we don't use input(I can't see the output without it)
#         with sp.Popen(['sqlplus','system/euLagoon2710@'+db,'@sql_script.sql'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.PIPE) as com:
#             out,err = com.communicate()
#             file.writelines('\n')
#             file.writelines('\n')
#             file.writelines('\n')
#             file.writelines(f'###################################'+'\n')
#             file.writelines(f'DATA From database {db}:')
#             for line in out.decode().splitlines():
#                 file.writelines(line+'\n')

for instance in list_of_db:
    connection =  cx_Oracle.connect(user="zportal", password="Minas_13Lugrom",
                                       dsn=instance)

    with open('output_'+instance+'.csv','w') as file:
        writer = csv.writer(file)
        cursor = connection.cursor()
        result = cursor.execute('''select count(1) from zportal.users where userid in (3164083020,
2258808015,
2081734021,
3054258020,
2649230015,
1535825027,
1896612027,
62357468004,
62567793031,
2493915020,
290761026,
3643382020,
2390272020,
2523091015,
2458785015,
3357613020,
2232318015,
1495092027,
3729725020,
2177739014,
2488209015,
62595121031,
3360388020,
3721387020,
1541900027,
2298385015,
1851466027,
1863946027,
211569040,
2277924015,
2650028015,
2233486015,
3296388020,
1991524021,
1921221027,
2097322021,
405113026,
2448979015,
2510171036,
1531386027,
1943160027,
2549680015,
3048603020,
2510616015,
2225494015,
2203692014,
3439126020,
2395369015,
1967439027,
396639026,
1596738027,
62584272031,
2501930020,
3520391020,
2421267015,
214174030,
62390341012,
1965673021,
2368761015,
2472762015,
3359650020,
281532026,
1704834021,
62580840031,
3745099020,
3237817020,
2636349015,
1918528021,
2067661020,
62357481008,
3763612020,
2197382014,
2322883020,
3459027020,
2679587015,
2429353015,
3540241020,
2221350015,
2637243015,
392517026,
3628414020,
3360787020,
2177498014,
3535320020,
292688026,
1760852027,
2734411020,
1938270027,
62477191008,
313225026,
1519631027,
1908400027,
3307387020,
3741178020,
62593233031,
2324380015,
62307105023,
2190901015,
2497955036,
2901175020,
2352497020,
2663762015,
1981183027,
2325837015,
161960040,
2238149015,
2623877015,
62438813012,
2175616014,
2476962020,
2461533036,
62632115031,
1630968027,
2225795015,
1591496027,
1599393027,
1743947027,
2364481015,
1836698027,
2410655020,
1719444027,
62391166012,
62640421031,
3500523020,
2367272020,
2598901015,
2312254015,
3117356020,
2344685015,
2396539020,
2546963015,
1581073027,
2653821015,
2009103021,
2343837015,
384455026,
2471075015,
2380694020,
2051815021,
1642363027,
3607601020,
3546021020,
2947545020,
3305301020,
1927782027,
62591532031,
2263604015,
62419160004,
1723640027,
2503745015,
3521753020,
2434335015,
1959466027,
2434015020,
1834625027,
3765719020,
282562026,
62314710023,
2198653014,
1900897027,
62390889012,
2670937015,
2428435015,
2203128014,
2661297015,
412319026,
3467101020,
2358866020,
3762977020,
62325470023,
2375770020,
1937631027,
3412049020,
1879110021,
62357291008,
1588326027,
1529460027,
2203138014,
2490565020,
2431134015,
3364441020,
3089675020,
62556477031,
1827684027,
2382796020,
2228344015,
3364588020,
62620129031,
2601972015,
3477281020,
2648510020,
2493668015,
3421451020,
62344977023,
1537389027,
1943448027,
2393617020,
2054644021,
2522357020,
281482026,
1555939027,
2633925015,
2443499036,
3687496020,
2218521015,
3591571020,
175993040,
3763815020,
1639237027,
3608931020,
3285789020,
3401562020,
1563610027,
3717142020,
1792805027,
156699040,
2439455015,
2298018015,
1933231021,
62631794031,
62426548023,
3385694020,
502773040,
3263315020,
2520812015,
2307116015,
3469767020,
62596629031,
294494026,
2130918014,
1985662027,
2206723015,
62584591031,
409258026,
2662843015,
2215405015,
3463244020,
1941043027,
3282147020,
2394622015,
62616792031,
2247742015,
1932367021,
229056030,
1896851027,
3302167020,
2637554015,
2660886015,
3557089020,
1549728027,
62440098004,
2435395015,
2426735015,
1562116027,
62463144008,
1786748027,
3532115020,
311138026,
2606925015,
62302308023,
2583600015,
2331677015,
2345588015,
62564627031,
219228030,
1808888027,
3511526020,
2065776021,
62458530008,
62567932031,
1520518027,
2635258015,
2687750015,
3404638020,
1539094027,
1695784027,
2365229020,
1784555027,
1741816027,
1964270021,
3161652020,
3311389020,
2218479015,
1931479021,
2473969015,
139524035,
1496319027,
1989117027,
1624410027,
2185481015,
2537194015,
2523516015,
2188814014,
1719488027,
336551040,
62603992031,
2536954015,
62340744008,
3279302020,
217142040,
2624062015,
1759249027,
2278981015,
1818925027,
192641040,
1919451021,
62580237031,
1704445027,
3626629020,
1743326027,
1761624021,
3668029020,
2588731015,
3506266020,
1634593027,
2371460015,
3603532020,
1585747027,
1599931027,
3641027020,
1845983027,
3652241020,
177586040,
2193924015,
3561047020,
62574608031,
2539345015,
2467787015,
1747732027,
2455667015,
3589632020,
1701680027,
3439115020,
2078836021,
1533252027,
2566903015,
3672567020,
2633931015,
1565990027,
2453493020,
1515477027,
189412040,
2422797015,
3407538020,
2241958015,
184586040,
1578064027,
3405482020,
1701471021,
294541026,
2014941027,
3724247020,
2506189015,
2190024014,
3040098020,
1612355027,
2646601020,
3269336020,
2323690015,
3644316020,
2213149015,
1629495027,
1974480027,
62632867031,
2357959015,
1587849027,
2316679020,
3312461020,
2097377021,
1863823027,
2549696015,
3306720020,
2461159015,
1647650027,
62630396031,
3487803020,
2039391021,
2471588015,
2613416015,
3402086020,
3466622020,
1559187027,
3278718020,
3365709020,
2404979020,
2391939015,
1760315027,
1662014027,
2183431014,
406631026,
164382040,
1777456027,
1681427027,
213656030,
221827030,
1660718027,
3408941020,
362093026,
62616926031,
1808194027,
2206243015,
2357102015,
1746273027,
1638942027,
2350328015,
2064253021,
2471774015,
62500959004,
1490108027,
2370611015,
2646116015,
62609990031,
62367268008,
278896026,
3578583020,
195551040,
2007736027,
62402861012,
167902040,
2190789014,
1522490027,
2320996020,
401104040,
1790179027,
3583297020,
2505682036,
3632923020,
1539131027,
174672040,
206342040,
1563955027,
2480310015,
2058156021,
2210189015,
2423782015,
3604908020,
3365168020,
2373598015,
1640655027,
1620648027,
3657197020,
287276026,
356379026,
2684920015,
62468642008,
1942257021,
219330040,
62563168031,
2532343015,
2653664015,
2162405014,
3576158020,
2534545015,
3732384020,
2518368036,
3054240020,
3660618020,
3666054020,
62414300004,
3265125020,
2125341014,
3753676020,
2359644020,
1535116027,
1992179027,
62321287004,
1527952027,
2514242015,
1545996027,
3435834020,
2453984020,
3703901020,
1590350027,
2897609020,
3373543020,
62574927031,
2216163015,
2327674015,
3302798020,
2562424015,
1840807027,
2507855020,
1577208027,
3291315020,
1578112027,
2930350020,
1730108027,
3241436020,
2480843015,
62309724023,
225269030,
156770041,
62561621031,
3546188020,
271414026,
2470770015,
2401601020,
2328485015,
1869531021,
1828279027,
3411721020,
2305292015,
2648402015,
3244610020,
1512177027,
2349036015,
62608308031,
3315552020,
2601302015,
2501175020,
3412563020,
2032020021,
3745320020,
2242807015,
3491275020,
2416195020,
2467385015,
405046026,
2661078015,
2526902015,
1970888027,
2492567015,
3607675020,
1835274027,
3360154020,
2508647015,
1555357027,
3631165020,
2334605015,
2465323015,
2370404015,
62390001008,
2198616015,
1826275027,
2615950020,
1751258027,
2277659015,
1647698027,
2484801015,
2446870015,
191885040,
308365026,
1996424027,
3242762020,
62477140008,
211727040,
3302255020,
2181878014,
285783026,
2215051015,
1990680021,
2665869015,
1489120027,
2305476020,
1719207027,
1760895027,
2338730020,
2512583015,
1537839027,
2474490015,
1780874027,
2428675015,
3096192020,
3057629020,
3314990020,
62362368008,
2328590015,
1750964027,
2012785027,
1854013027,
309315026,
1562620027,
1514852027,
2401939015,
2426687015,
2151668014,
3396556020,
1890190027,
1696292027,
3396138020,
3666893020,
203059040,
3544351020,
3389246020,
1892970027,
62564564031,
2479956015,
3364677020,
193996040,
2541292015,
2562026015,
3421438020,
1909309027,
1499348027,
2617117015,
1591624027,
1810992027,
2532741015,
3079347020,
2565700015,
2653528015,
1699525027,
2086623021,
1723506027,
3547793020,
3721536020,
3244321020,
1527446027,
3499603020,
3133687020,
62339884004,
3269053020,
336420026,
2318988015,
2170817014,
1921128027,
3714394020,
1799581027,
2563839015,
2392995015,
359311026,
1846684027,
3230179020,
2374153036,
1548901027,
1527767027,
3265408020,
229298030,
3201142020,
2358769015,
3311495020,
1892104027,
3423714020,
1696974021,
1508558027,
2321547020,
2453310015,
2582804015,
2415410015,
3757563020,
1673561027,
2258453015,
1636369027,
3408562020,
1863333027,
2006259027,
2031812005,
1606271027,
3649646020,
2096319021,
1826028027,
3055189020,
1769142027,
2084398021,
2378161020,
3565013020,
3644742020,
2017030027,
1858750027,
2488060015,
3377468020,
3522731020,
2412697015,
1518611027,
1966027021,
2042723021,
2621054015,
1804349027,
2618504015,
1599607027,
2518775015,
3052589020,
2312471015,
1936387027,
415112026,
1755475027,
2282799015,
3358941020,
2602572015,
3557499020,
1673637027,
3413277020,
2599560015,
3262265020,
1995274021,
1811743027,
1919955027,
3646875020,
157940040,
3695109020,
3754824020,
1614465027,
2127115014,
62614616031,
1549389027,
3691581020,
1753582027,
62609573031,
1924192027,
2068481020,
2143778014,
3587346020,
62349470008,
3387614020,
3595834020,
1766816027,
3284307020,
3475908020,
1807988027,
1555116027,
62439489004,
2210234015,
3364933020,
62632132031,
62437555004,
2208817015,
2234184015,
2329671015,
3530236020,
213800040,
62366522004,
62605010031,
1683366027,
3089003020,
1827560027,
3541552020,
1730547027,
2678512015,
1955561027,
2225979015,
62357135008,
3674731020,
3308225020,
2458851015,
1828857027,
3421527020,
3253472020,
2132225014,
1519078027,
185434040,
2640304015,
2617074020,
214923030,
62571993031,
212279030,
62404264004,
1591213027,
2629441015,
2543047036,
2565857015,
62446647012,
2045416021,
1857488027,
1826236027,
2126551014,
2609193015,
3264484020,
2507982015,
1951048027,
2041346005,
3053201020,
2344299015,
302472026,
1771920027,
3439775020,
62403377012,
3517037020,
2007041027,
359838026,
2276256015,
2627896015,
2585639015,
2612509015,
285158026,
2253743020,
1488925027,
1927839027,
3395402020,
1767011027,
62608026031,
1630686027,
2495806015,
3517072020,
1970708027,
281213026,
3523240020,
164733040,
62392192004,
3549685020,
3048117020,
192580040,
214939030,
3181183020,
3567714020,
1935454027,
2247513015,
2199011014,
2504676036,
2421030036,
293983026,
2479647015,
2167465014,
359573026,
1603926027,
353886026,
405410026,
2649567020,
2097994021,
2360836015,
2416434015,
2491338015,
1920248021,
1862871027,
2219797015,
2321296015,
3308238020,
2954580020,
2574025015,
1927682027,
2196502014,
1709460021,
3616160020,
62619876031,
3523337020,
3667464020,
2375060020,
3581155020,
3763010020,
1999317021,
2637411015,
1566077027,
3397753020,
3681906020,
1856102027,
3087083020,
1921660027,
339248026,
2198666014,
2178062014,
2040952021,
62640642031,
1995710027,
3026160020,
62481382008,
1555807027,
62425428012,
2234280020,
2467321015,
2308414015,
1554762027,
62469628008,
2423656015,
196839040,
168932040,
2454995015,
2559451015,
3584370020,
62391007004,
2240719015,
2637246015,
189601040,
1769075027,
1901174027,
1507904027,
3274641020,
3655990020,
2531290015,
2065952021,
1555932027,
1820121027,
3046542020,
62559878031,
2372787015,
62566739031,
280577026,
2668476015,
2595543015,
1995263027,
2500367020,
62341191008,
2519081015,
3660464020,
62448432012,
2405563015,
62452385004,
1865088027,
3036698020,
2297083015,
2348453015,
62466552008,
62606675031,
2182979014,
2488827015,
2789357020,
3462073020,
62591287031,
2183433014,
2416228036,
62594124031,
3557929020,
1558543027,
1502732027,
1748570027,
3468644020,
1771007027,
2732183020,
3005214020,
2325369020,
2399655015,
62322017004,
2604150015,
2606260015,
2123867014,
2174906014,
62585921031,
1803915027,
2810232020,
157416041,
62512346004,
2345657015,
2225171015,
3540326020,
1668140027,
1628974027,
3413998020,
3504671020,
3545336020,
2253018015,
62316983008,
62620804031,
1490358027,
157636041,
2157820014,
2261983015,
1594815027,
2519826015,
1543750027,
1533378027,
62315055008,
1943334027,
1614544027,
62641766031,
2192513014,
1525055027,
1957797027,
3407655020,
3240640020,
3744303020,
3044273020,
3454833020,
2153413014,
272111026,
2176111014,
2363121015,
2234893015,
2372084015,
2036880021,
62293720023,
2493535015,
2314916020,
3577818020,
62577957031,
2164610014,
62361880023,
306322026,
2562892015,
1967497021,
1965370027,
280223026,
2021551021,
1723360027,
3053718020,
3305316020,
2317156020,
3242667020,
2183015014,
2619928020,
374623026,
1938579027,
3307522020,
1759863027,
3264461020,
1520204027,
3280887020,
1747711027,
1973956021,
1580021027,
2636366015,
1508576027,
1735143027,
2514089015,
2490168015,
1590477027,
3657506020,
2440535015,
2017600027,
3154040020,
2236428015,
1918862021,
1928412027) or userid in(
3650740020,
2562809015,
2034855021,
3293916020,
1606199027,
62404359023,
1723628027,
3111113020,
2481471036,
1908031027,
2237851015,
1696732027,
2202025015,
1896974027,
3360179020,
1804821027,
2414615015,
1991979021,
3147259020,
2461697015,
3626654020,
2245276015,
1747297027,
1813194027,
336222026,
2184054014,
2350646015,
309896026,
305032026,
2296382015,
1772861027,
1765952021,
2032193005,
2017035027,
1623882027,
3208153020,
3395067020,
3476539020,
2515836015,
62620553031,
62458158008,
2264916020,
3438524020,
1592078027,
3680394020,
2371783020,
2614442015,
1941497027,
2523803015,
2485205015,
2842565020,
3722150020,
3312200020,
1898294027,
2564228015,
2275438015,
3652723020,
1842284027,
2588266020,
3006323020,
1923528021,
3155805020,
192413040,
1520081027,
2343680015,
2501211020,
3443678020,
2218626015,
62625102031,
1973866021,
1497428027,
2186579015,
169783040,
2675126015,
2277914015,
219683030,
2006041027,
3286983020,
1993687027,
2418580036,
2260860015,
2461616015,
2669764015,
62382621008,
2187717014,
1496511027,
3296291020,
2505700015,
157784041,
1667762021,
3023894020,
2598911015,
1752316027,
3262289020,
2240574015,
3283195020,
2170173014,
1490293027,
3382919020,
62642048031,
1539400027,
1742813027,
3537831020,
1752381027,
2665285015,
3414299020,
2217765015,
3515427020,
415815026,
1502875027,
2360413015,
2444162015,
2131431014,
2188244014,
2422688015,
2206152015,
1774793027,
2198430014,
2419052015,
2350366015,
293749026,
2532492015,
62315312008,
3406181020,
3689467020,
2607780015,
2167114014,
1522902027,
2564232015,
2197262015,
1510928027,
268746026,
1655566027,
401169026,
2681801015,
2431640020,
384512026,
1929428027,
62409253012,
2160599014,
2522582015,
1695892027,
1925598021,
1898950027,
1655296027,
1790783027,
2133029014,
268936041,
2019875021,
62494815004,
359632026,
1630973027,
1965145027,
1619478027,
2607262015,
62298775023,
62337483004,
1588281027,
62301719023,
2401091015,
1943753021,
3735762020,
2125604014,
2160544014,
1554473027,
2324821015,
3147658020,
2256915015,
1866785027,
2552332036,
1610047027,
1585423027,
1971878027,
2367306015,
62459127008,
2324920020,
2680809015,
2682645015,
2026820005,
62615449031,
281509026,
1864466027,
3656959020,
2460939015,
2800881020,
3673319020,
3708139020,
1498089027,
2597211015,
3708971020,
2496441036,
2281669015,
159208040,
2622369015,
62564026031,
2302801015,
2189372014,
1971249021,
1965392027,
2017571021,
62399148012,
2296602015,
2362864020,
271691026,
211687040,
2479203015,
62471808004,
3564401020,
2416536020,
3625775020,
3161183020,
2432251015,
2193516014,
183295040,
2388939036,
1965680027,
143061041,
2633440015,
3672609020,
2651228015,
2154516014,
3160870020,
62398766012,
1863099027,
2265445015,
3499756020,
2626688020,
2562228015,
2327400015,
62294120023,
2363039015,
1521120027,
2439037015,
2677247020,
1823855027,
3682236020,
2597701015,
2033264021,
62356974008,
3653034020,
62321382004,
2324453015,
1588098027,
3503474020,
1519387027,
2162871014,
3034567020,
3442828020,
2231610015,
2214743015,
62426149023,
1899685027,
3565314020,
3386105020,
2259449015,
3656106020,
62566254031,
1850969027,
1750892027,
1793688027,
1666785027,
2131338014,
1909942027,
1817671027,
1668964027,
2325249015,
2285935015,
3033804020,
3645473020,
2931663020,
62566481031,
2078170021,
3307377020,
2231520015,
3238925020,
2039902021,
2193437014,
3672721020,
2406318020,
2357334015,
1880920027,
62445263004,
2207243015,
1501001027,
2360559015,
396001026,
2440822015,
362346026,
3469563020,
2065808021,
2405889015,
2111861020,
62449459012,
62403667012,
2575670015,
2665289015,
3703813020,
2665787015,
2328511015,
3657570020,
2188285015,
3433024020,
2192077015,
2412996015,
3616532020,
3397396020,
1560076027,
1677211027,
2453964020,
2618038015,
2335634015,
2190089014,
1820898027,
2324545020,
62567064031,
3626373020,
1609281027,
2573322015,
2394222015,
62620329031,
2212710015,
1654719027,
3032007020,
1991124021,
1939800021,
2320716015,
471615009,
1746753027,
2094089021,
385625026,
3276196020,
1556751027,
3270642020,
337937026,
2342210015,
2031221021,
1519511027,
1593169027,
2653687015,
1642853021,
1950418027,
2220592015,
62357171008,
303704026,
2372207015,
2445639015,
62574561031,
3299809020,
1997943027,
62399153023,
3734025020,
62351705004,
2516160015,
1516567027,
1973805021,
2347016020,
2105667020,
2570567015,
3478322020,
62420109012,
2545599015,
2271818015,
62639769031,
3292722020,
3722452020,
1957080027,
2346958015,
1646334027,
2619693020,
2434516015,
62404910004,
297946026,
62320935023,
1977847027,
2995065020,
62417227012,
1524844027,
3373325020,
62631545031,
2278395015,
2459589015,
1775525027,
1761604027,
62361601008,
3631115020,
1499455027,
185343040,
3636057020,
166964040,
168570040,
2432547015,
1504949027,
3131052020,
62642028031,
2185340014,
1890310027,
2001709021,
62624120031,
2165356014,
62570131031,
2192628015,
2162916014,
1633630027,
2425473015,
3192652020,
2454283015,
3652733020,
302037026,
408907026,
2664075015,
2428758015,
3039379020,
2399417020,
270959026,
310607026,
1942286027,
2511966015,
216672030,
2568912015,
193321040,
2011122021,
2489135015,
3417884020,
2565593015,
2753410020,
2542764015,
1507545027,
62314823023,
1497024027,
62569314031,
62603061031,
2555375020,
1819244027,
1591010027,
62566841031,
1502606027,
1740077027,
3100378020,
403041026,
2420770015,
2030321021,
62646222031,
2167618014,
197354037,
3652897020,
2489187015,
1682573027,
1771619027,
62630560031,
1689925027,
2006210027,
3733947020,
2556407015,
2222155015,
1593416027,
405646026,
2277287015,
1765548027,
2189842015,
2528234015,
3102864020,
62437410012,
1487256027,
3577118020,
2008651021,
3731729020,
2561888015,
351501026,
1773473021,
62389430023,
3205521020,
3036760020,
1605960027,
1594028027,
2188183014,
1489844027,
2443941015,
2323996015,
2201002014,
1541819027,
1599745027,
2516274036,
3096182020,
2518459015,
1603259027,
182025037,
3165144020,
62632460031,
1810871027,
3275323020,
2316689020,
2444606015,
2170701014,
2465930036,
415036026,
62316746008,
1765948021,
2220548015,
3409962020,
3549511020,
1585576027,
328234026,
2375242036,
2602981015,
217860030,
2464354015,
1971452021,
2214645015,
3116769020,
3279666020,
2462362015,
3134269020,
2337598015,
399332026,
3442757020,
1885905027,
2359375020,
363152026,
2602210015,
3440317020,
3473291020,
1535174027,
3420968020,
1664927027,
2189708014,
2606873015,
1772126027,
2406000015,
62589065031,
2589180015,
2154558014,
2661926015,
3273285020,
1643773027,
3085937020,
2453057015,
3094065020,
1823153027,
3590415020,
2316341015,
62315617008,
2261146015,
62370842008,
3511865020,
62632605031,
167976040,
2898115020,
2571335015,
1974756027,
2346661015,
2458950015,
3076129020,
3050531020,
2476224015,
1520019027,
1752724027,
2199991014,
1561492027,
2729313020,
2402534036,
144037041,
62593107031,
3290923020,
3095421020,
62317976008,
3708613020,
62413568012,
409417026,
2165608014,
1899230027,
62341206008,
2273766015,
1683039027,
62649367031,
2200846014,
2223149015,
1511930027,
3249404020,
3540277020,
1629497027,
1697988027,
1554770027,
3657012020,
62418898012,
2187309014,
62571414031,
3373556020,
2756396020,
2430135015,
2001837021,
227585030,
295438026,
285259026,
2538344015,
2003942027,
2389568015,
2490706015,
174828040,
2090891021,
3421059020,
62376060008,
2167827014,
2427166020,
62632952031,
2168224014,
62340097008,
2479317015,
2170904014,
156178041,
3034175020,
3592413020,
2423357036,
62349444008,
1733746021,
62349549008,
2613376015,
1585155027,
1558649027,
1858948021,
297413022,
3727317020,
3725223020,
3283428020,
1836607027,
2563984015,
1958908027,
2266961015,
3643146020,
2146618014,
3192955020,
2490193015,
2571238015,
1703720027,
363969026,
392416026,
2491991036,
2571961015,
2448296015,
2517004015,
2047201021,
1966504021,
411734026,
2144981014,
2434929020,
3176642020,
3071240020,
3255832020,
62367561023,
3686986020,
62436109012,
2571850015,
1694026027,
2643253015,
2493576036,
3415824020,
2483464036,
2138813014,
2058240021,
62558023031,
1611573027,
1889233027,
1506797027,
1903926027,
1908558027,
3080650020,
2243194015,
1685678027,
2652786015,
1504168027,
1565171027,
1539503027,
1583648027,
3426982020,
3020019020,
2325147020,
3314319020,
2623153015,
3557657020,
2309359015,
2489263015,
62608271031,
3275477020,
2243053015,
1809629027,
2065689021,
1615953027,
2273610015,
1542053027,
2643064015,
2431493036,
3623029020,
3042455020,
3755934020,
2444363036,
2564485015,
62561091031,
1737194027,
1584271027,
1937979027,
62338877004,
1562599027,
2548846015,
2222333015,
3103896020,
3528208020,
1643335027,
1555335027,
2425997015,
295023026,
3236619020,
3591105020,
2234424015,
2620018020,
2617405015,
2559860015,
1829463027,
1836254027,
2216787015,
2493286015,
3077049020,
3364178020,
2259483020,
2325092015,
1862520021,
3562307020,
2687724015,
190413037,
2478215015,
62438000004,
2614358015,
1971291021,
1894112027,
2164912014,
1803792027,
2520279015,
1892440027,
1557742027,
1511944027,
3523748020,
2215315015,
62308207023,
2206644015,
2205378015,
3467164020,
2227130015,
3274645020,
2328429015,
2449486015,
1523733027,
3152326020,
2215977015,
2438765015,
3716672020,
3385958020,
2499306036,
2453302015,
2371021015,
1933266027,
1501360027,
62560860031,
62444806012,
379687026,
171042040,
2325502020,
2671600015,
62400040012,
2139298014,
2304553015,
62416204012,
62603325031,
2864770020,
3027150020,
2676020015,
62357210008,
2172109020,
2391169015,
1780505027,
2167460014,
3665940020,
2359182020,
1839987021,
2413595036,
3232899020,
1773999021,
2606201015,
1937851021,
159108041,
2435393015,
2486812015,
1528716027,
1671308027,
1880767027,
3106376020,
1814885027,
2037097021,
62441470012,
62393104012,
329055026,
1526225027,
1507158027,
1521162027,
2663533015,
2316128015,
62616117031,
1665288021,
3731865020,
2614567015,
3583425020,
2224800015,
2201677015,
2532797015,
2186235015,
2487850015,
62630125031,
62556643031,
62325041023,
2443019036,
1745684027,
280790026,
2256676015,
2501669020,
62609307031,
3147335020,
3647565020,
2578627015,
1948076021,
1977834027,
2235432015,
3469458020,
3283091020,
2247531015,
2415140015,
195266040,
2555158015,
62474449008,
2189163014,
3430254020,
2416886015,
1760623027,
312106026,
392148026,
1925239027,
1550651027,
3595655020,
1765690027,
2506794015,
2639210015,
2151670014,
395101026,
402366026,
3308372020,
352539026,
2624086015,
2026017021,
3309703020,
2168250014,
2462155015,
279685026,
1605792027,
1769637027,
2888163020,
3112889020,
1670223027,
3476519020,
2227988015,
1747410027,
2255474015,
175056040,
2052288021,
62478378004,
2220952015,
62579843031,
1586670027,
1603763027,
186806040,
2390908015,
2092425021,
2541537036,
1556255027,
220530040,
3203539020,
227881030,
62456217008,
2526272015,
2037609021,
2577002015,
1505297027,
305387026,
2650925015,
1968819021,
1971930021,
2303949015,
2816060020,
3374622020,
1568649027,
2649363020,
1929482027,
1541299027,
2648153015,
3409056020,
382708026,
227613030,
2130801014,
2143761014,
2158061014,
219926030,
1966726027,
2177597014,
3306058020,
2324650015,
62571590031,
1586280027,
397838026,
313280026,
2061121021,
2658950015,
2518219015,
62631760031,
2262493015,
2654246015,
310637026,
3625323020,
2017293021,
3408899020,
1723586027,
405418026,
1737626027,
2660630015,
62327304023,
2263047015,
1924847021,
3146132020,
2568629015,
275577026,
2520481015,
2422930015,
3019268020,
2204347015,
62446752012,
3266563020,
62379721023,
3096653020,
1765300021,
62317550008,
2433569015,
2203619014,
3584123020,
3291367020,
1675713027,
2149915014,
1607268027,
292287026,
2654937015,
1698008027,
2526742015,
291171026,
62457411023,
1653603027,
62335263004,
1751673027,
1835187027,
2064011021,
1940087021,
2150232014,
1604188027,
1773532021,
62450289004,
3720409020,
3553820020,
1723145027,
2246747015,
3657638020,
62322006023,
2495798015,
3654426020,
280508026,
2550319015,
1497696027,
216422030,
1911059027,
2230529015,
3292067020,
1631312027,
3237815020,
2316725020,
3500041020,
2464702020,
2635429015,
3455772020,
2195626014,
3679692020,
3432912020,
2496307015,
359277026,
397794026,
2322946015,
2758092020,
2336226015) or userid in (
2488816015,
296177026,
2002836021,
3568415020,
2297024015,
2526067015,
2187868015,
2183351014,
1669114027,
2559609015,
1500970027,
2085437021,
1614419027,
62367984008,
2253214020,
1821601027,
1879381021,
1810696027,
2172020014,
2075246021,
2329621015,
1593897027,
141473041,
2145455014,
3402051020,
3189815020,
364851026,
1811983027,
3309603020,
62409181023,
1500566027,
2504164015,
1515952027,
1488113027,
62298701023,
374164026,
62422612012,
2681360015,
2184985014,
295608026,
3733535020,
2574748015,
1593069027,
1853342021,
193004040,
2577479015,
3377649020,
3505905020,
3655036020,
3397152020,
2142605014,
1991823021,
173732040,
2184077014,
62422210012,
1633263027,
1789550027,
3550692020,
62436720012,
3042811020,
2737779020,
1685345027,
62365790008,
2138821014,
304391026,
364243026,
2028428021,
2172443014,
2551815015,
3283050020,
1683610027,
2237032015,
2085741021,
2199728014,
175247040,
3645951020,
2128950014,
2471630015,
2103289021,
2583692015,
2328706015,
3716987020,
175838040,
62409072012,
3101379020,
2504552015,
1521609027,
373046026,
3311561020,
2140973014,
1822709027,
1910328027,
62611329031,
62387310008,
2181272014,
1807711027,
62396063023,
2669257015,
3359517020,
1737441027,
2453039015,
355159026,
3199938020,
2185666014,
156184041,
2626805015,
2659079015,
62320389023,
3727771020,
2451416020,
3305943020,
2293900015,
2473783015,
3692467020,
1948215021,
2073136021,
1572787027,
2172204020,
2142394014,
2434190020,
2479233015,
1655770027,
2546453015,
318242026,
2470613015,
1727373027,
3076614020,
62562482031,
62361591008,
2414153015,
2395159015,
2040444021,
62480959008,
1563209027,
2579176015,
3690600020,
2523294015,
2079919021,
62558407031,
2531128015,
2684399015,
2538942015,
2956198020,
2278941015,
150364041,
2271457020,
1579979027,
62609576031,
2954220020,
3359468020,
2382023015,
169602040,
2088800021,
62613207031,
2449027015,
2142574014,
2318949015,
2431883015,
1547852027,
1761224021,
2156210014,
3391801020,
1777900027,
2686007015,
62466869008,
3478356020,
2370470020,
62592520031,
62402160004,
3177355020,
3563420020,
2252365020,
1647860027,
2561236015,
1677781027,
3146902020,
3093454020,
2404689020,
2218085015,
2132465014,
1666583027,
3092148020,
2209014015,
2638202015,
2100281020,
159952041,
2542721015,
3081630020,
2008640027,
2513246020,
3088389020,
1609669027,
1617245021,
2502734020,
2008691021,
2653022015,
317934026,
2292822015,
62603200031,
1777553027,
62397666012,
62400521012,
2155506014,
2051686021,
3315919020,
2930803020,
2652772015,
1605760027,
2590526015,
62699354007,
2297171015,
3206087020,
62585499031,
1915209021,
2453959015,
2555417015,
2562064015,
1966427021,
2212793015,
212159030,
62572388031,
2685881015,
1700777027,
2327365015,
2351229015,
1611136027,
2200466014,
3414673020,
402866026,
3089400020,
1656359027,
3420676020,
2491228015,
2167083014,
62403880012,
62590833031,
62403470012,
62589390031,
2620094015,
2221999015,
3241173020,
2253975020,
2364423020,
1853103027,
3577196020,
2197264015,
2439531015,
3657644020,
2736747020,
1995045021,
397145026,
2646012015,
3415271020,
3568398020,
2167443020,
62355419004,
359065026,
1850904027,
2368344015,
1915903021,
1588585027,
1693634027,
2410658036,
1991763027,
2551541036,
3403006020,
1806571027,
3395384020,
2358427015,
2391985015,
3414223020,
3438408020,
1611780027,
1924130021,
2657703015,
2536285015,
2653211015,
2411877015,
2523073015,
62481097008,
2432223015,
3660778020,
1997286027,
3386009020,
2556992015,
223387040,
3744707020,
1762971027,
2194207014,
2984703020,
2162873014,
229237030,
3160824020,
2794551020,
1699547027,
62294054023,
2520283015,
2506199020,
2596970015,
1972397021,
2168567014,
1675172027,
2260030015,
2375980015,
2512625036,
2368126015,
2538918015,
3227422020,
2028462021,
1618004027,
2590370020,
2500904036,
2661009015,
62360138008,
1694386027,
374627026,
2977814020,
3546156020,
3708424020,
62630384031,
294673026,
3019186020,
1907663027,
62454148008,
2552021015,
2152941014,
2318939015,
360683026,
2196879015,
3749079020,
62499127004,
62563046031,
3199625020,
2589695015,
2492446015,
3195734020,
62402535012,
1842819027,
2336664015,
2206015015,
2323669020,
2171542014,
2634634020,
62318717004,
3024991020,
2479817015,
2177960014,
62598421031,
2995726020,
2164604014,
62430293012,
1772502027,
2027280020,
2414119015,
1623100027,
1704243021,
2505302015,
212583030,
1642400027,
1899722027,
3387874020,
354368026,
397221026,
2507042015,
2168405014,
62596707031,
2379871020,
2454983015,
2371582020,
1826633027,
2526913036,
2235449015,
151650041,
3036453020,
62632940031,
3570919020,
3365943020,
3262894020,
3544058020,
1607672027,
62632258031,
1584462027,
3281181020,
2201520015,
3408475020,
3263770020,
2643647015,
162388040,
2567236015,
2572002015,
2796499020,
3469449020,
3493762020,
1778308021,
2535501015,
1958623021,
2537305015,
1882491027,
2053411021,
1503454027,
62316760008,
3315692020,
305289026,
3633213020,
3574987020,
2127439014,
287686026,
2438634015,
2526879036,
1966664027,
2261239015,
1960177021,
1790789027,
1910028027,
404541026,
2521646015,
3394528020,
2407681036,
62605080031,
3407030020,
366077026,
1734873027,
3755254020,
1671471027,
62426185012,
2393205015,
3708819020,
2036835021,
2510919015,
3076296020,
3566895020,
2605210020,
3057703020,
2337976015,
2005891027,
2433741015,
62332477004,
2082911021,
158978040,
2506353015,
1764510027,
2485607015,
228123040,
62640089031,
2461632015,
2432927036,
318624026,
62448114008,
3311453020,
2199695014,
2257508015,
3394397020,
2566912015,
3597075020,
3607659020,
3315057020,
2227344015,
1529565027,
1993870021,
2531832015,
1949366021,
191578037,
2143421014,
2508847020,
3730041020,
2213202015,
2582008015,
3385929020,
1853114027,
3434602020,
2683679015,
307031026,
2463468015,
2467466015,
2177671014,
1940186027,
2058600021,
2420560015,
2152168014,
3731051020,
62471497004,
2527744036,
1607270027,
3044910020,
2734937020,
1580383027,
2545654015,
1510560027,
213699030,
3151105020,
1761595021,
1882347027,
2319100020,
3463204020,
1775278027,
1496766027,
2840400020,
1734445027,
1977062027,
3579291020,
2652707015,
3449258020,
2000799021,
2240466015,
2135710014,
1993234027,
3651790020,
2977122020,
2009457021,
2530905036,
361268026,
62296445023,
62341561023,
309161022,
3295906020,
1806926027,
3316273020,
3088099020,
1850437021,
2391542015,
3157582020,
2289933015,
2062165020,
3293924020,
2602784015,
2293842015,
62361605008,
2586583015,
2038654021,
1647680027,
3756910020,
62622878031,
1490098027,
3713521020,
1622083027,
1873431021,
2646670015,
3435792020,
2159149014,
1888367027,
1562856027,
2247411015,
2587484020,
2406868015,
1728416027,
177521040,
2416335015,
2169758014,
62346886004,
360426026,
351299026,
2460682015,
2366896015,
3762580020,
1599329027,
3154255020,
62388829012,
362865026,
3527159020,
62342189004,
2650909020,
3100883020,
62479742008,
2563950015,
362692026,
1886581027,
1539024027,
3398111020,
1643442027,
2446812015,
1670404027,
3173733020,
3168557020,
62594462031,
62385686008,
2462589015,
2470370015,
2625380015,
62567864031,
1604363027,
1829870021,
2521516015,
2546961015,
3461896020,
2789363020,
3684140020,
1928317027,
227075030,
226053030,
1511141027,
1781427021,
2404249015,
2252287015,
2164706014,
2515863020,
2458885015,
1616400021,
174692040,
2201797015,
2223313015)''')
        writer.writerows(result)

