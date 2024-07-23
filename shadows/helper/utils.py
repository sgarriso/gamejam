if __import__("sys").platform == "emscripten":
    from platform import window
    



def save_object(key, object):
    window.localStorage.setItem(key, str(object) )

def restore_object(key):
    return window.localStorage.getItem(key)
    
def delete_objects():
    keys = []
    for i in range(window.localStorage.length):
        keys.append(window.localStorage.key(i))
    while keys: window.localStorage.removeItem(keys.pop())