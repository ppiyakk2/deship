import rethinkdb as r


def get_connected_servers():
    con = r.connect()
    l = list(r.db('rethinkdb').table('server_status').run(con))
    return l


def get_all_servers():
    con = r.connect()
    l = list(r.db('rethinkdb').table('table_config').
             concat_map(lambda x: x['shards']).
             concat_map(lambda c: c['replicas']).distinct().run(con))
    return l


def get_throughput():
    con = r.connect()
    result = r.db("rethinkdb").table("stats").get(["cluster"]).run(con)
    read_sec = result['query_engine']['read_docs_per_sec']
    write_sec = result['query_engine']['written_docs_per_sec']
    return read_sec, write_sec
