from pyspark.sql import *
from pyspark.sql.functions import *

from pyspark.sql import *
from pyspark.sql.functions import *

from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.functions import *

spark=SparkSession.builder.appName("test").master("local[*]").getOrCreate()
spark.conf.set("spark.sql.legacy.timeParserPolicy","LEGACY")
from pyspark.sql import *
from pyspark.sql.functions import *
spark=SparkSession.builder.appName("test").master("local[*]").getOrCreate()
data=r"C:\Users\mouni\Desktop\world_bank.json"
df=spark.read.format("json").option("header","true").option("mode", "DROPMALFORMED").load(data)
# df.show()
#extract using col(loc)[0]
# df2=df.withColumn("lang",col("loc")[0]).withColumn("latitude",col("loc")[1])
# df.show()
df.printSchema()
#handling
df2=df.withColumn("them1name",col("theme1.name")).withColumn("theme1precent",col("theme1.percent")).drop("theme1")
df2.show()
df3=df2.withColumn("theme_namecode",explode(col("theme_namecode")))\
.withColumn("theme_name_name",col("theme_namecode.name"))\
.withColumn("theme_name_code",col("theme_namecode.code"))\
.drop("theme_namecode")
df3.show()
# df2.printSchema()
#
# | -- theme1: struct(nullable=true)
# | | -- Name: string(nullable=true)
# | | -- Percent: long(nullable=true)
# | -- theme_namecode: array(nullable=true)
# | | -- element: struct(containsNull=true)
# | | | -- code: string(nullable=true)
# | | | -- name: string(nullable=true)
# | -- themecode: string(nullable=true)
# | -- totalamt: long(nullable=true)
# | -- totalcommamt: long(nullable=true)
# | -- url: string(nullable=true)
