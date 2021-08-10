print('Játszunk egy kérdez-feleleket egy storyval, például mi lenne ha 2 iker Henrik és Hanna akiktől amegkérdezed hogy jönnek-e kosarazni én meg válaszolok.')
a = input('Henrik jönn ma kosarazni? igen vagy nem válasz!')
b = input('Hanna jönn ma kosarazni? igen vagy nem válasz!')

if a == 'igen' and b == 'igen':
    print('mind a ketten jönnek kosarazni.')
elif a == 'igen' and b == 'nem':
    print('csak az egyikük jön kosarazni.')
elif a == 'nem' and b == 'igen':
    print('csak az egyikük jön kosarazni.')
else:
    print('egyikük sem jön kosarazni')

    
