from pushbullet import Pushbullet

pb = Pushbullet("o.2oZ8cwzqJaRUSlU18oP8EEn0CpHGwyjS")

def send(person):
    push = pb.push_note("Birthday", person)