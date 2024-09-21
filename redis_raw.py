import redis

redis_conn = redis.Redis(host='localhost', port=6379, db=0)

# para insert e update
redis_conn.set("chave_1", "trocando_o_meu_valor")

# select
meu_valor = redis_conn.get("chave_1").decode("utf-8")

# delete de dados
redis_conn.delete("chave_1")

print(meu_valor)
print(type(meu_valor))
