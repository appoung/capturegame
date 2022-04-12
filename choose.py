import random
member = ["한병준","임준혁","정연우","김동현","임성준"]
password_list = ['0325','1103']
def chooseRole():
    spy = random.choice(member)
    return spy
def chooseTeam(spy):
    global member
    member.remove(spy)
    team1 = random.sample(member, 2)
    team2 = list(set(member) - set(team1))
    return team1,team2
    member = ["한병준","임준혁","정연우","김동현","임성준"]