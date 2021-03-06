from pyspark.sql import SQLContext
sqlContext = SQLContext(sc)
sqlContext.setConf("spark.sql.parquet.binaryAsString", "true")
df = sqlContext.read.parquet("hdfs://cluster019.test.local/events/testparquet/*.parq")
df.printSchema()
df.show()
df.select("receipttime").show()

root
 |-- agentaddress: string (nullable = true)
 |-- agentdescriptorid: string (nullable = true)
 |-- agentdnsdomain: string (nullable = true)
 |-- agenthostname: string (nullable = true)
 |-- agentid: string (nullable = true)
 |-- agentmacaddress: string (nullable = true)
 |-- agentntdomain: string (nullable = true)
 |-- agentreceipttime: long (nullable = true)
 |-- agenttimezone: string (nullable = true)
 |-- agenttranslatedaddress: string (nullable = true)
 |-- agenttranslatedzoneexternalid: string (nullable = true)
 |-- agenttranslatedzonereferenceid: string (nullable = true)
 |-- agenttranslatedzoneuri: string (nullable = true)
 |-- agenttype: string (nullable = true)
 |-- agentversion: string (nullable = true)
 |-- agentzoneexternalid: string (nullable = true)
 |-- agentzonereferenceid: string (nullable = true)
 |-- agentzoneuri: string (nullable = true)
 |-- applicationprotocol: string (nullable = true)
 |-- assetcriticality: string (nullable = true)
 |-- baseeventcount: long (nullable = true)
 |-- baseeventids: string (nullable = true)
 |-- bytesin: long (nullable = true)
 |-- bytesout: long (nullable = true)
 |-- categorybehavior: string (nullable = true)
 |-- categorycustomformatfield: string (nullable = true)
 |-- categorydescriptorid: string (nullable = true)
 |-- categorydevicegroup: string (nullable = true)
 |-- categorydevicetype: string (nullable = true)
 |-- categoryobject: string (nullable = true)
 |-- categoryoutcome: string (nullable = true)
 |-- categorysignificance: string (nullable = true)
 |-- categorytechnique: string (nullable = true)
 |-- categorytupledescription: string (nullable = true)
 |-- cryptosignature: string (nullable = true)
 |-- customerexternalid: string (nullable = true)
 |-- customerreferenceid: string (nullable = true)
 |-- customeruri: string (nullable = true)
 |-- destinationaddress: string (nullable = true)
 |-- destinationdnsdomain: string (nullable = true)
 |-- destinationgeocountrycode: string (nullable = true)
 |-- destinationgeodescriptorid: string (nullable = true)
 |-- destinationgeolatitude: float (nullable = true)
 |-- destinationgeolocationinfo: string (nullable = true)
 |-- destinationgeolongitude: float (nullable = true)
 |-- destinationgeopostalcode: string (nullable = true)
 |-- destinationgeoregioncode: string (nullable = true)
 |-- destinationhostname: string (nullable = true)
 |-- destinationmacaddress: string (nullable = true)
 |-- destinationntdomain: string (nullable = true)
 |-- destinationport: long (nullable = true)
 |-- destinationprocessid: string (nullable = true)
 |-- destinationprocessname: string (nullable = true)
 |-- destinationservicename: string (nullable = true)
 |-- destinationtranslatedaddress: string (nullable = true)
 |-- destinationtranslatedport: long (nullable = true)
 |-- destinationtranslatedzoneexternalid: string (nullable = true)
 |-- destinationtranslatedzonereferenceid: string (nullable = true)
 |-- destinationtranslatedzoneuri: string (nullable = true)
 |-- destinationuserid: string (nullable = true)
 |-- destinationusername: string (nullable = true)
 |-- destinationuserprivileges: string (nullable = true)
 |-- destinationzoneexternalid: string (nullable = true)
 |-- destinationzonereferenceid: string (nullable = true)
 |-- destinationzoneuri: string (nullable = true)
 |-- deviceaction: string (nullable = true)
 |-- deviceaddress: string (nullable = true)
 |-- devicecustomdate1: long (nullable = true)
 |-- devicecustomdate1label: string (nullable = true)
 |-- devicecustomdate2: long (nullable = true)
 |-- devicecustomdate2label: string (nullable = true)
 |-- devicecustomdescriptorid: string (nullable = true)
 |-- devicecustomfloatingpoint1: float (nullable = true)
 |-- devicecustomfloatingpoint1label: string (nullable = true)
 |-- devicecustomfloatingpoint2: float (nullable = true)
 |-- devicecustomfloatingpoint2label: string (nullable = true)
 |-- devicecustomfloatingpoint3: float (nullable = true)
 |-- devicecustomfloatingpoint3label: string (nullable = true)
 |-- devicecustomfloatingpoint4: float (nullable = true)
 |-- devicecustomfloatingpoint4label: string (nullable = true)
 |-- devicecustomipv6address1: string (nullable = true)
 |-- devicecustomipv6address1label: string (nullable = true)
 |-- devicecustomipv6address2: string (nullable = true)
 |-- devicecustomipv6address2label: string (nullable = true)
 |-- devicecustomipv6address3: string (nullable = true)
 |-- devicecustomipv6address3label: string (nullable = true)
 |-- devicecustomipv6address4: string (nullable = true)
 |-- devicecustomipv6address4label: string (nullable = true)
 |-- devicecustomnumber1: long (nullable = true)
 |-- devicecustomnumber1label: string (nullable = true)
 |-- devicecustomnumber2: long (nullable = true)
 |-- devicecustomnumber2label: string (nullable = true)
 |-- devicecustomnumber3: long (nullable = true)
 |-- devicecustomnumber3label: string (nullable = true)
 |-- devicecustomnumber4: long (nullable = true)
 |-- devicecustomnumber4label: string (nullable = true)
 |-- devicecustomnumber5: long (nullable = true)
 |-- devicecustomnumber5label: string (nullable = true)
 |-- devicecustomnumber6: long (nullable = true)
 |-- devicecustomnumber6label: string (nullable = true)
 |-- devicecustomstring1: string (nullable = true)
 |-- devicecustomstring1label: string (nullable = true)
 |-- devicecustomstring2: string (nullable = true)
 |-- devicecustomstring2label: string (nullable = true)
 |-- devicecustomstring3: string (nullable = true)
 |-- devicecustomstring3label: string (nullable = true)
 |-- devicecustomstring4: string (nullable = true)
 |-- devicecustomstring4label: string (nullable = true)
 |-- devicecustomstring5: string (nullable = true)
 |-- devicecustomstring5label: string (nullable = true)
 |-- devicecustomstring6: string (nullable = true)
 |-- devicecustomstring6label: string (nullable = true)
 |-- devicedescriptorid: string (nullable = true)
 |-- devicedirection: string (nullable = true)
 |-- devicednsdomain: string (nullable = true)
 |-- devicedomain: string (nullable = true)
 |-- deviceeventcategory: string (nullable = true)
 |-- deviceeventclassid: string (nullable = true)
 |-- deviceexternalid: string (nullable = true)
 |-- devicefacility: string (nullable = true)
 |-- devicehostname: string (nullable = true)
 |-- deviceinboundinterface: string (nullable = true)
 |-- devicemacaddress: string (nullable = true)
 |-- devicentdomain: string (nullable = true)
 |-- deviceoutboundinterface: string (nullable = true)
 |-- devicepayloadid: string (nullable = true)
 |-- deviceprocessid: string (nullable = true)
 |-- deviceprocessname: string (nullable = true)
 |-- deviceproduct: string (nullable = true)
 |-- devicereceipttime: long (nullable = true)
 |-- deviceseverity: string (nullable = true)
 |-- devicetimezone: string (nullable = true)
 |-- devicetranslatedaddress: string (nullable = true)
 |-- devicetranslatedzoneexternalid: string (nullable = true)
 |-- devicetranslatedzonereferenceid: string (nullable = true)
 |-- devicetranslatedzoneuri: string (nullable = true)
 |-- devicevendor: string (nullable = true)
 |-- deviceversion: string (nullable = true)
 |-- devicezoneexternalid: string (nullable = true)
 |-- devicezonereferenceid: string (nullable = true)
 |-- devicezoneuri: string (nullable = true)
 |-- domainexternalid: string (nullable = true)
 |-- domainid: string (nullable = true)
 |-- domainreferenceid: string (nullable = true)
 |-- domainuri: string (nullable = true)
 |-- endtime: long (nullable = true)
 |-- eventannotationaudittrail: string (nullable = true)
 |-- eventannotationcomment: string (nullable = true)
 |-- eventannotationendtime: long (nullable = true)
 |-- eventannotationeventid: string (nullable = true)
 |-- eventannotationflags: string (nullable = true)
 |-- eventannotationmanagerreceipttime: long (nullable = true)
 |-- eventannotationmodificationtime: long (nullable = true)
 |-- eventannotationmodifiedbyexternalid: string (nullable = true)
 |-- eventannotationmodifiedbyreferenceid: string (nullable = true)
 |-- eventannotationmodifiedbyuri: string (nullable = true)
 |-- eventannotationstageeventid: string (nullable = true)
 |-- eventannotationstageexternalid: string (nullable = true)
 |-- eventannotationstagereferenceid: string (nullable = true)
 |-- eventannotationstageupdatetime: long (nullable = true)
 |-- eventannotationstageuri: string (nullable = true)
 |-- eventannotationstageuserexternalid: string (nullable = true)
 |-- eventannotationstageuserreferenceid: string (nullable = true)
 |-- eventannotationstageuseruri: string (nullable = true)
 |-- eventannotationversion: string (nullable = true)
 |-- eventid: long (nullable = true)
 |-- eventoutcome: string (nullable = true)
 |-- externalid: string (nullable = true)
 |-- filecreatetime: long (nullable = true)
 |-- filehash: string (nullable = true)
 |-- fileid: string (nullable = true)
 |-- filemodificationtime: long (nullable = true)
 |-- filename: string (nullable = true)
 |-- filepath: string (nullable = true)
 |-- filepermission: string (nullable = true)
 |-- filesize: long (nullable = true)
 |-- filetype: string (nullable = true)
 |-- flexdate1: long (nullable = true)
 |-- flexdate1label: string (nullable = true)
 |-- flexnumber1: long (nullable = true)
 |-- flexnumber1label: string (nullable = true)
 |-- flexnumber2: long (nullable = true)
 |-- flexnumber2label: string (nullable = true)
 |-- flexstring1: string (nullable = true)
 |-- flexstring1label: string (nullable = true)
 |-- flexstring2: string (nullable = true)
 |-- flexstring2label: string (nullable = true)
 |-- generatorexternalid: string (nullable = true)
 |-- generatorreferenceid: string (nullable = true)
 |-- generatoruri: string (nullable = true)
 |-- locality: string (nullable = true)
 |-- managerreceipttime: long (nullable = true)
 |-- message: string (nullable = true)
 |-- modelconfidence: string (nullable = true)
 |-- name: string (nullable = true)
 |-- oldfilecreatetime: long (nullable = true)
 |-- oldfilehash: string (nullable = true)
 |-- oldfileid: string (nullable = true)
 |-- oldfilemodificationtime: long (nullable = true)
 |-- oldfilename: string (nullable = true)
 |-- oldfilepath: string (nullable = true)
 |-- oldfilepermission: string (nullable = true)
 |-- oldfilesize: long (nullable = true)
 |-- oldfiletype: string (nullable = true)
 |-- oldfsize: long (nullable = true)
 |-- originator: string (nullable = true)
 |-- persistence: string (nullable = true)
 |-- priority: string (nullable = true)
 |-- product: string (nullable = true)
 |-- prop_sign_ver_date: string (nullable = true)
 |-- proto: string (nullable = true)
 |-- rawevent: string (nullable = true)
 |-- reason: string (nullable = true)
 |-- receipttime: long (nullable = true)
 |-- relevance: string (nullable = true)
 |-- requestclientapplication: string (nullable = true)
 |-- requestcontext: string (nullable = true)
 |-- requestcookies: string (nullable = true)
 |-- requestmethod: string (nullable = true)
 |-- requesturl: string (nullable = true)
 |-- rulethreadid: string (nullable = true)
 |-- sessionid: string (nullable = true)
 |-- severity: string (nullable = true)
 |-- signature: string (nullable = true)
 |-- sourceaddress: string (nullable = true)
 |-- sourcednsdomain: string (nullable = true)
 |-- sourcegeocountrycode: string (nullable = true)
 |-- sourcegeodescriptorid: string (nullable = true)
 |-- sourcegeolatitude: float (nullable = true)
 |-- sourcegeolocationinfo: string (nullable = true)
 |-- sourcegeolongitude: float (nullable = true)
 |-- sourcegeopostalcode: string (nullable = true)
 |-- sourcegeoregioncode: string (nullable = true)
 |-- sourcehostname: string (nullable = true)
 |-- sourcemacaddress: string (nullable = true)
 |-- sourcentdomain: string (nullable = true)
 |-- sourceport: long (nullable = true)
 |-- sourceprocessid: string (nullable = true)
 |-- sourceprocessname: string (nullable = true)
 |-- sourceservicename: string (nullable = true)
 |-- sourcetranslatedaddress: string (nullable = true)
 |-- sourcetranslatedport: long (nullable = true)
 |-- sourcetranslatedzoneexternalid: string (nullable = true)
 |-- sourcetranslatedzonereferenceid: string (nullable = true)
 |-- sourcetranslatedzoneuri: string (nullable = true)
 |-- sourceuserid: string (nullable = true)
 |-- sourceusername: string (nullable = true)
 |-- sourceusernameuniqueid: string (nullable = true)
 |-- sourceuserprivileges: string (nullable = true)
 |-- sourcezoneexternalid: string (nullable = true)
 |-- sourcezonereferenceid: string (nullable = true)
 |-- sourcezoneuri: string (nullable = true)
 |-- starttime: long (nullable = true)
 |-- transportprotocol: string (nullable = true)
 |-- type: string (nullable = true)
 |-- vendor: string (nullable = true)
 |-- vulnerabilityexternalid: string (nullable = true)
 |-- vulnerabilityreferenceid: string (nullable = true)
 |-- vulnerabilityuri: string (nullable = true)
 |-- xagentreceipttimelocal: long (nullable = true)
 |-- xdestinationuniqueuserid: long (nullable = true)
 |-- xdestinationusernameoriginal: string (nullable = true)
 |-- xreceipttimelocal: long (nullable = true)
 |-- xsourceusernameoriginal: string (nullable = true)
 |-- xsourceuseruniqueid: long (nullable = true)
 |-- xuniqueeventid: long (nullable = true)
 |-- xunmapped: string (nullable = true)

+--------------+-----------------+--------------+--------------------+--------------------+---------------+-------------+----------------+------------------+----------------------+-----------------------------+------------------------------+----------------------+---------+------------+-------------------+--------------------+--------------------+-------------------+----------------+--------------+------------+-------+--------+----------------+-------------------------+--------------------+-------------------+------------------+--------------+---------------+--------------------+-----------------+------------------------+---------------+------------------+-------------------+--------------------+------------------+--------------------+-------------------------+--------------------------+----------------------+--------------------------+-----------------------+------------------------+------------------------+-------------------+---------------------+-------------------+---------------+--------------------+----------------------+----------------------+----------------------------+-------------------------+-----------------------------------+------------------------------------+----------------------------+-----------------+-------------------+-------------------------+-------------------------+--------------------------+------------------+------------+--------------+-----------------+----------------------+-----------------+----------------------+------------------------+--------------------------+-------------------------------+--------------------------+-------------------------------+--------------------------+-------------------------------+--------------------------+-------------------------------+------------------------+-----------------------------+------------------------+-----------------------------+------------------------+-----------------------------+------------------------+-----------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+--------------------+------------------------+------------------+---------------+---------------+------------+--------------------+------------------+----------------+--------------+--------------------+----------------------+----------------+--------------+-----------------------+---------------+---------------+-----------------+-------------+-----------------+--------------+------------------+-----------------------+------------------------------+-------------------------------+-----------------------+------------+-------------+--------------------+---------------------+--------------------+----------------+--------+-----------------+---------+-------+-------------------------+----------------------+----------------------+----------------------+--------------------+---------------------------------+-------------------------------+-----------------------------------+------------------------------------+----------------------------+---------------------------+------------------------------+-------------------------------+------------------------------+-----------------------+----------------------------------+-----------------------------------+---------------------------+----------------------+-------+------------+----------+--------------+--------+------+--------------------+--------+--------+--------------+--------+--------+---------+--------------+-----------+----------------+-----------+----------------+-----------+----------------+-----------+----------------+-------------------+--------------------+------------+--------+------------------+-------+---------------+--------------------+-----------------+-----------+---------+-----------------------+-----------+-----------+-----------------+-----------+-----------+--------+----------+-----------+--------+-------+------------------+-----+--------+------+-------------+---------+------------------------+--------------+--------------+-------------+----------+------------+---------+--------+---------+-------------+---------------+--------------------+---------------------+-----------------+---------------------+------------------+-------------------+-------------------+--------------+----------------+--------------+----------+---------------+-----------------+-----------------+-----------------------+--------------------+------------------------------+-------------------------------+-----------------------+------------+--------------+----------------------+--------------------+--------------------+---------------------+-------------+---------+-----------------+----+------+-----------------------+------------------------+----------------+----------------------+------------------------+----------------------------+-----------------+-----------------------+-------------------+--------------+---------+
|  agentaddress|agentdescriptorid|agentdnsdomain|       agenthostname|             agentid|agentmacaddress|agentntdomain|agentreceipttime|     agenttimezone|agenttranslatedaddress|agenttranslatedzoneexternalid|agenttranslatedzonereferenceid|agenttranslatedzoneuri|agenttype|agentversion|agentzoneexternalid|agentzonereferenceid|        agentzoneuri|applicationprotocol|assetcriticality|baseeventcount|baseeventids|bytesin|bytesout|categorybehavior|categorycustomformatfield|categorydescriptorid|categorydevicegroup|categorydevicetype|categoryobject|categoryoutcome|categorysignificance|categorytechnique|categorytupledescription|cryptosignature|customerexternalid|customerreferenceid|         customeruri|destinationaddress|destinationdnsdomain|destinationgeocountrycode|destinationgeodescriptorid|destinationgeolatitude|destinationgeolocationinfo|destinationgeolongitude|destinationgeopostalcode|destinationgeoregioncode|destinationhostname|destinationmacaddress|destinationntdomain|destinationport|destinationprocessid|destinationprocessname|destinationservicename|destinationtranslatedaddress|destinationtranslatedport|destinationtranslatedzoneexternalid|destinationtranslatedzonereferenceid|destinationtranslatedzoneuri|destinationuserid|destinationusername|destinationuserprivileges|destinationzoneexternalid|destinationzonereferenceid|destinationzoneuri|deviceaction| deviceaddress|devicecustomdate1|devicecustomdate1label|devicecustomdate2|devicecustomdate2label|devicecustomdescriptorid|devicecustomfloatingpoint1|devicecustomfloatingpoint1label|devicecustomfloatingpoint2|devicecustomfloatingpoint2label|devicecustomfloatingpoint3|devicecustomfloatingpoint3label|devicecustomfloatingpoint4|devicecustomfloatingpoint4label|devicecustomipv6address1|devicecustomipv6address1label|devicecustomipv6address2|devicecustomipv6address2label|devicecustomipv6address3|devicecustomipv6address3label|devicecustomipv6address4|devicecustomipv6address4label|devicecustomnumber1|devicecustomnumber1label|devicecustomnumber2|devicecustomnumber2label|devicecustomnumber3|devicecustomnumber3label|devicecustomnumber4|devicecustomnumber4label|devicecustomnumber5|devicecustomnumber5label|devicecustomnumber6|devicecustomnumber6label|devicecustomstring1|devicecustomstring1label|devicecustomstring2|devicecustomstring2label|devicecustomstring3|devicecustomstring3label|devicecustomstring4|devicecustomstring4label|devicecustomstring5|devicecustomstring5label| devicecustomstring6|devicecustomstring6label|devicedescriptorid|devicedirection|devicednsdomain|devicedomain| deviceeventcategory|deviceeventclassid|deviceexternalid|devicefacility|      devicehostname|deviceinboundinterface|devicemacaddress|devicentdomain|deviceoutboundinterface|devicepayloadid|deviceprocessid|deviceprocessname|deviceproduct|devicereceipttime|deviceseverity|    devicetimezone|devicetranslatedaddress|devicetranslatedzoneexternalid|devicetranslatedzonereferenceid|devicetranslatedzoneuri|devicevendor|deviceversion|devicezoneexternalid|devicezonereferenceid|       devicezoneuri|domainexternalid|domainid|domainreferenceid|domainuri|endtime|eventannotationaudittrail|eventannotationcomment|eventannotationendtime|eventannotationeventid|eventannotationflags|eventannotationmanagerreceipttime|eventannotationmodificationtime|eventannotationmodifiedbyexternalid|eventannotationmodifiedbyreferenceid|eventannotationmodifiedbyuri|eventannotationstageeventid|eventannotationstageexternalid|eventannotationstagereferenceid|eventannotationstageupdatetime|eventannotationstageuri|eventannotationstageuserexternalid|eventannotationstageuserreferenceid|eventannotationstageuseruri|eventannotationversion|eventid|eventoutcome|externalid|filecreatetime|filehash|fileid|filemodificationtime|filename|filepath|filepermission|filesize|filetype|flexdate1|flexdate1label|flexnumber1|flexnumber1label|flexnumber2|flexnumber2label|flexstring1|flexstring1label|flexstring2|flexstring2label|generatorexternalid|generatorreferenceid|generatoruri|locality|managerreceipttime|message|modelconfidence|                name|oldfilecreatetime|oldfilehash|oldfileid|oldfilemodificationtime|oldfilename|oldfilepath|oldfilepermission|oldfilesize|oldfiletype|oldfsize|originator|persistence|priority|product|prop_sign_ver_date|proto|rawevent|reason|  receipttime|relevance|requestclientapplication|requestcontext|requestcookies|requestmethod|requesturl|rulethreadid|sessionid|severity|signature|sourceaddress|sourcednsdomain|sourcegeocountrycode|sourcegeodescriptorid|sourcegeolatitude|sourcegeolocationinfo|sourcegeolongitude|sourcegeopostalcode|sourcegeoregioncode|sourcehostname|sourcemacaddress|sourcentdomain|sourceport|sourceprocessid|sourceprocessname|sourceservicename|sourcetranslatedaddress|sourcetranslatedport|sourcetranslatedzoneexternalid|sourcetranslatedzonereferenceid|sourcetranslatedzoneuri|sourceuserid|sourceusername|sourceusernameuniqueid|sourceuserprivileges|sourcezoneexternalid|sourcezonereferenceid|sourcezoneuri|starttime|transportprotocol|type|vendor|vulnerabilityexternalid|vulnerabilityreferenceid|vulnerabilityuri|xagentreceipttimelocal|xdestinationuniqueuserid|xdestinationusernameoriginal|xreceipttimelocal|xsourceusernameoriginal|xsourceuseruniqueid|xuniqueeventid|xunmapped|
+--------------+-----------------+--------------+--------------------+--------------------+---------------+-------------+----------------+------------------+----------------------+-----------------------------+------------------------------+----------------------+---------+------------+-------------------+--------------------+--------------------+-------------------+----------------+--------------+------------+-------+--------+----------------+-------------------------+--------------------+-------------------+------------------+--------------+---------------+--------------------+-----------------+------------------------+---------------+------------------+-------------------+--------------------+------------------+--------------------+-------------------------+--------------------------+----------------------+--------------------------+-----------------------+------------------------+------------------------+-------------------+---------------------+-------------------+---------------+--------------------+----------------------+----------------------+----------------------------+-------------------------+-----------------------------------+------------------------------------+----------------------------+-----------------+-------------------+-------------------------+-------------------------+--------------------------+------------------+------------+--------------+-----------------+----------------------+-----------------+----------------------+------------------------+--------------------------+-------------------------------+--------------------------+-------------------------------+--------------------------+-------------------------------+--------------------------+-------------------------------+------------------------+-----------------------------+------------------------+-----------------------------+------------------------+-----------------------------+------------------------+-----------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+-------------------+------------------------+--------------------+------------------------+------------------+---------------+---------------+------------+--------------------+------------------+----------------+--------------+--------------------+----------------------+----------------+--------------+-----------------------+---------------+---------------+-----------------+-------------+-----------------+--------------+------------------+-----------------------+------------------------------+-------------------------------+-----------------------+------------+-------------+--------------------+---------------------+--------------------+----------------+--------+-----------------+---------+-------+-------------------------+----------------------+----------------------+----------------------+--------------------+---------------------------------+-------------------------------+-----------------------------------+------------------------------------+----------------------------+---------------------------+------------------------------+-------------------------------+------------------------------+-----------------------+----------------------------------+-----------------------------------+---------------------------+----------------------+-------+------------+----------+--------------+--------+------+--------------------+--------+--------+--------------+--------+--------+---------+--------------+-----------+----------------+-----------+----------------+-----------+----------------+-----------+----------------+-------------------+--------------------+------------+--------+------------------+-------+---------------+--------------------+-----------------+-----------+---------+-----------------------+-----------+-----------+-----------------+-----------+-----------+--------+----------+-----------+--------+-------+------------------+-----+--------+------+-------------+---------+------------------------+--------------+--------------+-------------+----------+------------+---------+--------+---------+-------------+---------------+--------------------+---------------------+-----------------+---------------------+------------------+-------------------+-------------------+--------------+----------------+--------------+----------+---------------+-----------------+-----------------+-----------------------+--------------------+------------------------------+-------------------------------+-----------------------+------------+--------------+----------------------+--------------------+--------------------+---------------------+-------------+---------+-----------------+----+------+-----------------------+------------------------+----------------+----------------------+------------------------+----------------------------+-----------------+-----------------------+-------------------+--------------+---------+
|10.0.0.47|             null|          null|server1.test.l...|3G2NOiVEBABCAA6Cg...|           null|         null|   1460762332147|  Australia/Sydney|                  null|                         null|                          null|                  null|     winc|7.1.7.7600.0|               null|                null|/All Zones/ArcSig...|               null|            null|          null|        null|   null|    null|            null|                     null|                null|               null|Security Mangement|          null|           null|                null|             null|                    null|           null|              null|               null|/All Customers/UN...|              null|                null|                     null|                      null|                  null|                      null|                   null|                    null|                    null|               null|                 null|               null|           null|                null|                  null|                  null|                        null|                     null|                               null|                                null|                        null|             null|               null|                     null|                     null|                      null|              null|        null|10.0.0.47|    1460762032131|             Last time|             null|                  null|                    null|                      null|                           null|                      null|                           null|                      null|                           null|                      null|                           null|                    null|                         null|                    null|                         null|                    null|                         null|                    null|                         null|                  0|       Total event count|                  0|    Total raw event l...|                  0|       Event count (SLC)|               null|                    null|               null|                    null|               null|                    null|                0.0|        Event throughput|                0.0|    Raw event charact...|                0.0|    Event throughput ...|                  0|    Raw event length ...|                0.0|    Raw event charact...|3G2NOiVEBABCAA6Cg...|          Destination ID|              null|           null|           null|        null|/Agent/RawEvent/S...|              null|            null|          null|         DAUAA01S010|                  null|            null|          null|                   null|           null|           null|             null|     ArcSight|             null|       Warning|  Australia/Sydney|                   null|                          null|                           null|                   null|    ArcSight| 7.1.7.7600.0|                null|                 null|/All Zones/ArcSig...|            null|    null|             null|     null|   null|                     null|                  null|                  null|                  null|                null|                             null|                           null|                               null|                                null|                        null|                       null|                          null|                           null|                          null|                   null|                              null|                               null|                       null|                  null|    883|        null|      null|          null|    null|  null|                null|    null|    null|          null|    null|   Agent|     null|          null|       null|            null|       null|            null|       null|            null|       null|            null|               null|                null|        null|    null|     1460762332131|   null|           null|Connector Raw Eve...|             null|       null|     null|                   null|       null|       null|             null|       null|       null|    null|      null|       null|    null|   null|              null| null|    null|  null|1460762332131|     null|                    null|          null|          null|         null|      null|        null|     null|     Low|agent:050|         null|           null|                null|                 null|             null|                 null|              null|               null|               null|          null|            null|          null|      null|           null|             null|             null|                   null|                null|                          null|                           null|                   null|        null|          null|                  null|                null|                null|                 null|         null|     null|             null|null|  null|                   null|                    null|            null|         1460798332147|                    null|                        null|    1460798332131|                   null|               null|          null|     null|
|10.0.0.44|             null|          null|server2.test.l...|3Ppu2B1MBABCAAljx...|           null|         null|   1460725685816|Australia/Canberra|                  null|                         null|                          null|                  null|   syslog|7.1.7.7600.0|               null|                null|/All Zones/ArcSig...|               null|            null|          null|        null|   null|    null|            null|                     null|                null|               null|              null|          null|           null|                null|             null|                    null|           null|              null|               null|/All Customers/UN...|              null|                null|     


df.registerTempTable("cef")
qry = sqlContext.sql("select distinct destinationusername from cef")
qry.explain()
print qry.show()

== Physical Plan ==
TungstenAggregate(key=[destinationusername#60], functions=[], output=[destinationusername#60])
+- TungstenExchange hashpartitioning(destinationusername#60,200), None
   +- TungstenAggregate(key=[destinationusername#60], functions=[], output=[destinationusername#60])
      +- Scan ParquetRelation[destinationusername#60] InputPaths: hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.0.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.1.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.10.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.11.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.12.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.13.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.14.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.15.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.16.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.17.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.18.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.19.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.2.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.20.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.21.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.22.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.23.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.24.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.3.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.4.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.5.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.6.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.7.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.8.parq, hdfs://cluster019.test.local/events/testparquet/ac417ecc9dfecc90-734c6f1d3f2fee92_679359534_data.9.parq
+-------------------+
|destinationusername|
+-------------------+
|           arcsight|
|               null|
|        nagiosadmin|
+-------------------+


