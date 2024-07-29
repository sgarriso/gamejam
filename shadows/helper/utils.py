if __import__("sys").platform == "emscripten":
    from platform import window
import json
    



def save_object(key, object):
    
    window.localStorage.setItem(key, json.dumps(object))

def restore_object(key):
    try:
        results = window.localStorage.getItem(key)
        return json.loads(results)  if results  else results
    except:
        window.localStorage.removeItem(key)
        return None

    
def delete_objects():
    keys = []
    for i in range(window.localStorage.length):
        keys.append(window.localStorage.key(i))
    while keys: window.localStorage.removeItem(keys.pop())