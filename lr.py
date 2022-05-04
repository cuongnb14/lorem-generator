#!/usr/bin/env python3

import click
import random

seed = """purus quam duised etinteger justomauris vestibulumvivamus felis metuscras odiovestibulum laoreetproin magna consecteturinteger mi convallis viverra aliquam proin vitae pharetra placerat urna id sagittisinteger tortor aenean consectetur erat cursusaenean massaphasellus montes mattis nibh risusnulla eu urnaphasellus egestas per laoreet dictum sapienfusce vivamus penatibus tellusvestibulum etiam dui turpisinteger habitant facilisinunc viverranulla orcialiquam est sollicitudin ornare arcucurabitur suscipitvestibulum vulputate lobortis tempor gravidaaliquam porttitorvestibulum congue posuere fermentumut maximusinteger libero curabitur elitcras loremnam euismod turpiscras elitfusce temporproin ipsum in lacus lorem cras dignissim suscipitcurabitur integer porttitor sem accumsan natoque sapiendonec massa ut nulla odioetiam consecteturaenean inceptos ullamcorper diamnulla nonsuspendisse torquent nibhnam eratsed senectus leout velitphasellus potenti semperduis scelerisque nascetur hac vehicula erosquisque porta parturient aliquet habitasse volutpatin dictumstaliquam feugiatvivamus facilisis nislaliquam exdonec rhoncus nullam morbi conubia maurisnullam sollicitudinmorbi volutpataenean hendreritnullam semut vestibulumsuspendisse tristique mus tellus asuspendisse sapienmauris primis class blandit et quis fusce magnis ad felisvestibulum miut eratin iaculis portanunc nibhin sociosqu quisque nisi ac loremut semper enim curae luctus ultricies gravidaetiam felisnam ullamcorperaenean eleifend nullaut felispraesent gravidaduis sed sit quisut cursus odiopellentesque ridiculus loremin sollicitudinsed risus sodales feugiat velnunc at diam lectusphasellus ligulanam orci himenaeospraesent nunc nibhdonec vel dictumst dis duis sapien ex sempervestibulum atphasellus nuncphasellus felisnulla efficiturpraesent ligula massaaenean variusquisque velitpraesent amet tincidunt pulvinarmaecenas blanditaenean vestibulumvestibulum lectus ipsumin dictuminteger maurisnunc risusmaecenas netus nisl sagittis dapibus imperdiet elementum metusinteger turpis consequat litora suspendisse dolorduis himenaeos hendrerit massanullam facilisi lectusvestibulum nuncpraesent ligulaproin efficitur phasellus lacinia maecenas pulvinar aliquamsed a mollis odio loremnulla molestie cursussed pellentesque cubilia odionulla loreminteger donec suscipit volutpatut condimentum ultrices laoreetnulla faucibus nam pharetracurabitur necduis nec eniminteger quissuspendisse massacurabitur himenaeosfusce necin nequeinterdum varius fames rutrumcras condimentumsed enimvivamus pretium volutpat rutrum liberocurabitur eratinteger faucibusnam purusmaecenas fringillain necsuspendisse fringilla tinciduntetiam malesuada bibendum euismodmauris justo taciti platea aptent interdum lorempraesent finibusduis egestasquisque vestibulum velit ultricesaenean pretiummaecenas praesent variusetiam dolormaecenas etut finibus elit consecteturpraesent dolor neque tortorsed egestasnullam gravida ante mivestibulum maximus consequatsed metus leo eros velitin maurisvivamus commodo portanam augue consecteturvivamus faucibusaliquam fermentum venenatis auctor nostra diamnunc tempus mauris eget liberodonec sagittisphasellus adipiscing non egestasvestibulum arcu rutrumproin turpisdonec tempornunc"""

seed = seed.split(" ")

@click.command()
@click.argument('length', default=0)
@click.option('-p', '--paragraph', default=False, is_flag=True)
def lorem(paragraph, length):
    if paragraph:
        length = length if length else 3
        result = ''
        for i in range(length):
            result += ' '.join(random.choice(seed) for _ in range(random.randint(20, 30))).capitalize()
            result += '\n\n'
    else:
        length = length if length else 8
        result = ' '.join(random.choice(seed) for _ in range(length)).capitalize()

    print(result)

if __name__ == '__main__':
    lorem()
