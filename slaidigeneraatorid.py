from odfdo import *

def setAttributes(element, atribuudid):
    for i in atribuudid:
        element.set_attribute(i, atribuudid[i])

def setOfficeForms(page):
    officeForms = OfficeForms()
    setAttributes(officeForms, {
        'form:automatic-focus': 'false',
        'form:apply-design-mode': 'false'
        })
    page.append(officeForms)

def tumeTaustAll(page, ridade_arv):
    shape = Element.from_tag('draw:custom-shape')
    
    if ridade_arv == 1:
        setAttributes(shape, {
            'draw:style-name': 'gr16',
            'draw:text-style-name': 'P1',
            'draw:layer': 'layout',
            'svg:width': '28cm',
            'svg:height': '2.46cm',
            'svg:x': '0cm',
            'svg:y': '13.29cm'
            })
    if ridade_arv == 2:
        setAttributes(shape, {
            'draw:style-name': 'gr4',
            'draw:text-style-name': 'P1',
            'draw:layer': 'layout',
            'svg:width': '28cm',
            'svg:height': '3.5cm',
            'svg:x': '0cm',
            'svg:y': '12.25cm'
            })
    if ridade_arv == 3:
        setAttributes(shape, {
            'draw:style-name': 'gr10',
            'draw:text-style-name': 'P1',
            'draw:layer': 'layout',
            'svg:width': '28cm',
            'svg:height': '4.46cm',
            'svg:x': '0cm',
            'svg:y': '11.29cm'
            })
    
    shape.append(Paragraph(""))
    geom = Element.from_tag('draw:enhanced-geometry')
    setAttributes(geom, {
        'svg:viewBox': '0 0 21600 21600',
        'draw:type': 'rectangle',
        'draw:enhanced-path': 'M 0 0 L 21600 0 21600 21600 0 21600 0 0 Z N'
        })
    shape.append(geom)
    page.append(shape)



def uusPealkiri(slaidi_number, tekst, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp3',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TAGUMINE TUME ALA
    tumeTaustAll(page, 2)
    
    # TEKST
    shape = Element.from_tag('draw:custom-shape')
    setAttributes(shape, {
        'draw:style-name': 'gr5',
        'draw:text-style-name': 'P11',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '2.67cm',
        'svg:x': '1.4cm',
        'svg:y': '12.29cm'
        })
    text = Paragraph()
    setAttributes(text, {'text:style-name': 'P10'})
    span = Span(tekst)
    setAttributes(span, {'text:style-name': 'T8'})
    text.append(span)
    shape.append(text)
    page.append(shape)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)


def uusSalm(slaidi_number, tekst, pealkiri, number_txt, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp4',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # SÕNAD
    elemendid = []
    for i in tekst:
        text = Paragraph()
        span = Span(i)
        setAttributes(span, {'text:style-name': 'T9'})
        text.append(span)
        elemendid.append(text)
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'draw:style-name': 'gr6',
        'draw:text-style-name': 'P13',
        'draw:layer': 'layout',
        'svg:width': '23.7cm',
        'svg:height': '13.189cm',
        'svg:x': '2.2cm',
        'svg:y': '1.29cm'
        })
    page.append(frame)
    
    
    # ALUMISED TEKSTID
    alatekst = Paragraph()
    setAttributes(alatekst, {'text:style-name': 'P14'})
    span = Span(pealkiri)
    setAttributes(span, {'text:style-name': 'T10'})
    alatekst.append(span)
    
    salmiNumber = Paragraph()
    setAttributes(salmiNumber, {'text:style-name': 'P14'})
    span = Span(number_txt)
    setAttributes(span, {'text:style-name': 'T10'})
    salmiNumber.append(span)
    
    frame = Frame.text_frame([alatekst, salmiNumber])
    setAttributes(frame, {
        'draw:style-name': 'gr7',
        'draw:text-style-name': 'P15',
        'draw:layer': 'layout',
        'svg:width': '24cm',
        'svg:height': '2.612cm',
        'svg:x': '2.4cm',
        'svg:y': '12.964cm'
        })
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)

def ühereaTekst(slaidi_number, liturgia, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp3',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TUME TAUST TEKSTIDEL
    tumeTaustAll(page, 1)
    
    # TEKST
    tekst = Paragraph()
    setAttributes(tekst, {'text:style-name': 'P26'})
    span = Span(liturgia)
    setAttributes(span, {'text:style-name': 'T11'})
    tekst.append(span)
    frame = Frame.text_frame(tekst)
    setAttributes(frame, {
        'draw:style-name': 'gr13',
        'draw:text-style-name': 'P27',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '4.655cm',
        'svg:x': '1.4cm',
        'svg:y': '10.305cm'
        })
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)

def kahereaTekst(slaidi_number, liturgia, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp3',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TUME TAUST TEKSTIDEL
    tumeTaustAll(page, 2)
    
    # TEKST
    elemendid = []
    for i in liturgia:
        tekst = Paragraph()
        setAttributes(tekst, {'text:style-name': 'P26'})
        span = Span(i)
        setAttributes(span, {'text:style-name': 'T16'})
        tekst.append(span)
        elemendid.append(tekst)
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'draw:style-name': 'gr13',
        'draw:text-style-name': 'P27',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '2.453cm',
        'svg:x': '1.4cm',
        'svg:y': '12.507cm'
        })
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)
    

def kolmereaTekst(slaidi_number, kogu_tekst, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp3',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TUME TAUST TEKSTIDEL
    tumeTaustAll(page, 3)
    
    # TEKST
    tekst = Paragraph()
    setAttributes(tekst, {'text:style-name': 'P21'})
    span = Span(kogu_tekst)
    setAttributes(span, {'text:style-name': 'T11'})
    tekst.append(span)
    frame = Frame.text_frame(tekst)
    setAttributes(frame, {
        'draw:style-name': 'gr11',
        'draw:text-style-name': 'P22',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '3.67cm',
        'svg:x': '1.4cm',
        'svg:y': '11.29cm'
        })
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)


def lugemisePealkiri(slaidi_number, tekstid, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp3',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TUME TAUST TEKSTIDEL
    tumeTaustAll(page, 2)
    
    # TEKST
    elemendid = []
    for i in tekstid:
        tekst = Paragraph()
        setAttributes(tekst, {'text:style-name': 'P19'})
        span = Span(i)
        setAttributes(span, {'text:style-name': 'T12'})
        tekst.append(span)
        elemendid.append(tekst)
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'draw:style-name': 'gr5',
        'draw:text-style-name': 'P20',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '2.67cm',
        'svg:x': '1.4cm',
        'svg:y': '12.29cm'
        })
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)

def lugemiseTekst(slaidi_number, tekstid, salmi_number, praeguneRida, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp3',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TUME TAUST TEKSTIDEL
    tumeTaustAll(page, 3)
    
    # TEKST
    elemendid = []
    tekst = Paragraph()
    setAttributes(tekst, {'text:style-name': 'P26'})
    for i in tekstid:
        span = Span()
        span.clear()
        span.text = str(i)
        if salmi_number:
            setAttributes(span, {'text:style-name': 'T18'})
            salmi_number = False
        else:
            setAttributes(span, {'text:style-name': 'T11'})
            salmi_number = True
        tekst.append(span)
    elemendid.append(tekst)
    #print(rida)
    for i in range(2-praeguneRida):
        tühitekst = Paragraph()
        setAttributes(tühitekst, {'text:style-name': 'P26'})
        span = Span()
        setAttributes(span, {'text:style-name': 'T11'})
        span.append(Spacer())
        tühitekst.append(span)
        elemendid.append(tühitekst)
            
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'draw:style-name': 'gr17',
        'draw:text-style-name': 'P29',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '3.67cm',
        'svg:x': '1.4cm',
        'svg:y': '11.29cm'
        })
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)


def pealkiriMeile(slaidi_number, pealkiri, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp3',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TUME TAUST TEKSTIDEL
    tumeTaustAll(page, 2)
    
    # TEKST
    shape = Element.from_tag('draw:custom-shape')
    setAttributes(shape, {
        'draw:style-name': 'gr12',
        'draw:text-style-name': 'P24',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '2.67cm',
        'svg:x': '1.4cm',
        'svg:y': '12.29cm'
        })
    text = Paragraph()
    setAttributes(text, {'text:style-name': 'P23'})
    span = Span(pealkiri)
    setAttributes(span, {'text:style-name': 'T13'})
    text.append(span)
    shape.append(text)
    geom = Element.from_tag('draw:enhanced-geometry')
    setAttributes(geom, {
        'svg:viewBox': '0 0 21600 21600',
        'draw:type': 'rectangle',
        'draw:enhanced-path': 'M 0 0 L 21600 0 21600 21600 0 21600 0 0 Z N'
        })
    shape.append(geom)
    page.append(shape)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)


def avaleht(slaidi_number, tiitel, laulud, lugemised, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp1',
        'draw:master-page-name': 'Default',
        'presentation:presentation-page-layout-name': 'AL1T19'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TUME TAUST KESKEL, SEEGA ÄÄRTES PISUT HELEDAM
    shape = Element.from_tag('draw:custom-shape')
    setAttributes(shape, {
        'draw:style-name': 'gr1',
        'draw:text-style-name': 'P1',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '14.17cm',
        'svg:x': '1.4cm',
        'svg:y': '0.79cm'
        })
    shape.append(Paragraph(""))
    geom = Element.from_tag('draw:enhanced-geometry')
    setAttributes(geom, {
        'svg:viewBox': '0 0 21600 21600',
        'draw:type': 'rectangle',
        'draw:enhanced-path': 'M 0 0 L 21600 0 21600 21600 0 21600 0 0 Z N'
        })
    shape.append(geom)
    page.append(shape)
    
    
    # TIITEL
    elemendid = []
    tekst = Paragraph(tiitel[0])
    setAttributes(tekst, {'text:style-name': 'P2'})
    span = Span("\n" + tiitel[1])
    setAttributes(span, {'text:style-name': 'T1'})
    tekst.append(span)
    elemendid.append(tekst)
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'presentation:style-name': 'pr1',
        'draw:text-style-name': 'P1',
        'draw:layer': 'layout',
        'svg:width': '22.679cm',
        'svg:height': '2.431cm',
        'svg:x': '2.662cm',
        'svg:y': '1.324cm',
        'presentation:class': 'title',
        'presentation:user-transformed': 'true'
        })
    page.append(frame)
    
    # LAULUD
    shape = Element.from_tag('draw:custom-shape')
    setAttributes(shape, {
        'draw:style-name': 'gr2',
        'draw:text-style-name': 'P6',
        'draw:layer': 'layout',
        'svg:width': '12.6cm',
        'svg:height': '10.17cm',
        'svg:x': '1.5cm',
        'svg:y': '4.79cm'
        })
    
    for i in laulud:
        if type(i) == str:
            text = Paragraph()
            setAttributes(text, {'text:style-name': 'P3'})
            span = Span(i)
            setAttributes(span, {'text:style-name': 'T2'})
            text.append(span)
            shape.append(text)
            continue
        elif len(i) == 2 and len(i[0]) == 2:
            text = Paragraph()
            setAttributes(text, {'text:style-name': 'P3'})
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Spacer())
            text.append(span)
            
            span = Span(i[0])
            setAttributes(span, {'text:style-name': 'T3'})
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span(i[1])
            setAttributes(span, {'text:style-name': 'T3'})
            text.append(span)
            
            shape.append(text)
            continue
        
        elif len(i) == 2 and len(i[0]) == 1:
            text = Paragraph()
            setAttributes(text, {'text:style-name': 'P3'})
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span(i[0])
            setAttributes(span, {'text:style-name': 'T3'})
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span(i[1])
            setAttributes(span, {'text:style-name': 'T3'})
            text.append(span)
            
            shape.append(text)
            continue
        
        elif len(i) == 2 and len(i[0]) == 3:
            text = Paragraph()
            setAttributes(text, {'text:style-name': 'P3'})
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span(i[0])
            setAttributes(span, {'text:style-name': 'T3'})
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span(i[1])
            setAttributes(span, {'text:style-name': 'T3'})
            text.append(span)
            
            shape.append(text)
            continue
        
        elif len(i) == 1:
            text = Paragraph()
            setAttributes(text, {'text:style-name': 'P3'})
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            spacer = Spacer()
            setAttributes(spacer, {'text:c': '5'})
            span.append(spacer)
            text.append(span)
            
            span = Span(i[0])
            setAttributes(span, {'text:style-name': 'T3'})
            text.append(span)
            
            shape.append(text)
            continue
        
        elif len(i) == 3 and len(i[2]) == 1:
            text = Paragraph()
            setAttributes(text, {'text:style-name': 'P3'})
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span(i[0])
            setAttributes(span, {'text:style-name': 'T4'})
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T5'})
            spacer = Spacer()
            span.append(spacer)
            text.append(span)
            
            span = Span(i[1])
            setAttributes(span, {'text:style-name': 'T5'})
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            spacer = Spacer()
            setAttributes(spacer, {'text:c': '6'})
            span.append(spacer)
            span.append(i[2])
            text.append(span)
            shape.append(text)
            continue
        
        elif len(i) == 3 and len(i[2]) != 1:
            text = Paragraph()
            setAttributes(text, {'text:style-name': 'P3'})
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span(i[0])
            setAttributes(span, {'text:style-name': 'T4'})
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T5'})
            span.append(Spacer())
            text.append(span)
            
            span = Span(i[1])
            setAttributes(span, {'text:style-name': 'T5'})
            text.append(span)
            
            span = Span()
            setAttributes(span, {'text:style-name': 'T3'})
            span.append(Tab())
            text.append(span)
            
            span = Span(i[2])
            setAttributes(span, {'text:style-name': 'T3'})
            text.append(span)
            shape.append(text)
            continue
    
    shape.append(text)
    geom = Element.from_tag('draw:enhanced-geometry')
    setAttributes(geom, {
        'svg:viewBox': '0 0 21600 21600',
        'draw:type': 'rectangle',
        'draw:enhanced-path': 'M 0 0 L 21600 0 21600 21600 0 21600 0 0 Z N'
        })
    shape.append(geom)
    page.append(shape)
    
    
    # KIRJAKOHAD
    shape = Element.from_tag('draw:custom-shape')
    setAttributes(shape, {
        'draw:style-name': 'gr2',
        'draw:text-style-name': 'P8',
        'draw:layer': 'layout',
        'svg:width': '12.6cm',
        'svg:height': '10.17cm',
        'svg:x': '13.978cm',
        'svg:y': '4.79cm'
        })
    
    for i in lugemised:
        text = Paragraph()
        setAttributes(text, {'text:style-name': 'P7'})
        span = Span(i)
        if lugemised.index(i) == 0:
            setAttributes(span, {'text:style-name': 'T2'})
        else:
            setAttributes(span, {'text:style-name': 'T7'})
        text.append(span)
        shape.append(text)
    
    geom = Element.from_tag('draw:enhanced-geometry')
    setAttributes(geom, {
        'svg:viewBox': '0 0 21600 21600',
        'draw:type': 'rectangle',
        'draw:enhanced-path': 'M 0 0 L 21600 0 21600 21600 0 21600 0 0 Z N'
        })
    shape.append(geom)
    page.append(shape)
    
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)

def lõpuSoov(slaidi_number, read, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp4',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TEKST
    elemendid = []
    for i in read:
        text = Paragraph()
        setAttributes(text, {'text:style-name': 'P2'})
        span = Span(i)
        setAttributes(span, {'text:style-name': 'T23'})
        text.append(span)
        elemendid.append(text)
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'draw:style-name': 'gr45',
        'draw:text-style-name': 'P36',
        'draw:layer': 'layout',
        'svg:width': '20.414cm',
        'svg:height': '4.049cm',
        'svg:x': '3.793cm',
        'svg:y': '8.79cm'
        })
    
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)


def lõpuTiitrid(slaidi_number, tiitel, peategijad, tehnikatiim, vöörmündrid, lõpusoov, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp4',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TIITEL
    text = Paragraph()
    span = Span(tiitel)
    setAttributes(span, {'text:style-name': 'T24'})
    text.append(span)
    frame = Frame.text_frame(text)
    setAttributes(frame, {
        'presentation:style-name': 'pr3',
        'draw:text-style-name': 'P37',
        'draw:layer': 'layout',
        'svg:width': '25.199cm',
        'svg:height': '2.63cm',
        'svg:x': '1.401cm',
        'svg:y': '0.49cm',
        'presentation:class': 'title',
        'presentation:user-transformed': 'true'
        })
    page.append(frame)
    
    # PEATEGIJAD
    elemendid = []
    textList = List()
    setAttributes(textList, {'text:style-name': 'L2'})
    header = Element.from_tag('text:list-header')
    for i in peategijad:
        text = Paragraph()
        setAttributes(text, {'text:style-name': 'P38'})
        bold = False
        for l in i:
            span = Span()
            span.clear()
            span.text = l
            if bold:
                bold = False
                setAttributes(span, {'text:style-name': 'T26'})
            else:
                bold = True
                setAttributes(span, {'text:style-name': 'T25'})
            text.append(span)
        header.append(text)
        textList.append(header)
    frame = Frame.text_frame(textList)
    setAttributes(frame, {
        'presentation:style-name': 'pr4',
        'draw:text-style-name': 'P40',
        'draw:layer': 'layout',
        'svg:width': '22.6cm',
        'svg:height': '6.17cm',
        'svg:x': '2.1cm',
        'svg:y': '2.92cm',
        'presentation:class': 'outline',
        'presentation:user-transformed': 'true'
        })
    page.append(frame)
    
    
    # TEHNIKATIIM
    elemendid = []
    bold = True
    
    text = Paragraph()
    setAttributes(text, {'text:style-name': 'P41'})
    span = Span(tehnikatiim[0])
    setAttributes(span, {'text:style-name': 'T29'})
    text.append(span)
    elemendid.append(text)
    tehnikatiim = tehnikatiim[1:]
    
    for i in tehnikatiim:
        text = Paragraph()
        setAttributes(text, {'text:style-name': 'P41'})
        for l in i:
            span = Span()
            span.clear()
            span.text = l
            if bold:
                bold = False
                setAttributes(span, {'text:style-name': 'T30'})
            else:
                bold = True
                setAttributes(span, {'text:style-name': 'T31'})
            text.append(span)
        elemendid.append(text)
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'draw:style-name': 'gr47',
        'draw:text-style-name': 'P43',
        'draw:layer': 'layout',
        'svg:width': '9.5cm',
        'svg:height': '5.298cm',
        'svg:x': '5.1cm',
        'svg:y': '9.19cm'
        })
    page.append(frame)
    
    # VÖÖRMÜNDRID
    elemendid = []
    pealkiri = True
    for i in vöörmündrid:
        text = Paragraph()
        setAttributes(text, {'text:style-name': 'P44'})
        span = Span(i)
        if pealkiri:
            pealkiri = False
            setAttributes(span, {'text:style-name': 'T29'})
        else:
            setAttributes(span, {'text:style-name': 'T30'})
        text.append(span)
        elemendid.append(text)
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'draw:style-name': 'gr48',
        'draw:text-style-name': 'P45',
        'draw:layer': 'layout',
        'svg:width': '10cm',
        'svg:height': '3.843cm',
        'svg:x': '16cm',
        'svg:y': '9.1cm'
        })
    page.append(frame)
    
    
    # LÕPUSOOV
    text = Paragraph()
    setAttributes(text, {'text:style-name': 'P2'})
    span = Span(lõpusoov)
    setAttributes(span, {'text:style-name': 'T28'})
    text.append(span)
    frame = Frame.text_frame(text)
    setAttributes(frame, {
        'draw:style-name': 'gr46',
        'draw:text-style-name': 'P28',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '1.277cm',
        'svg:x': '1.1cm',
        'svg:y': '13.783cm'
        })
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)
    
    
    
    
def liturgiaKollane(slaidi_number, liturgia, body):
    page = DrawPage()
    setAttributes(page, {
        'draw:name': 'page'+slaidi_number,
        'draw:style-name': 'dp3',
        'draw:master-page-name': 'Default'
        })
    
    # OFFICEFORMS SEADISTUS
    setOfficeForms(page)
    
    # TUME TAUST TEKSTIDEL
    tumeTaustAll(page, 3)
    
    # LITURGIA
    elemendid = []
    for i in liturgia:
        if type(i) == str:
            text = Paragraph()
            setAttributes(text, {'text:style-name': 'P33'})
            span = Span(i)
            setAttributes(span, {'text:style-name': 'T20'})
            text.append(span)
            elemendid.append(text)
        else:
            for l in i:
                text = Paragraph()
                setAttributes(text, {'text:style-name': 'P33'})
                
                span = Span()
                setAttributes(span, {'text:style-name': 'T21'})
                span.append(Tab())
                text.append(span)
                
                span = Span(l)
                setAttributes(span, {'text:style-name': 'T21'})
                text.append(span)
                
                elemendid.append(text)
            
    frame = Frame.text_frame(elemendid)
    setAttributes(frame, {
        'draw:style-name': 'gr13',
        'draw:text-style-name': 'P18',
        'draw:layer': 'layout',
        'svg:width': '25.2cm',
        'svg:height': '4.655cm',
        'svg:x': '1.4cm',
        'svg:y': '10.305cm'
        })
    page.append(frame)
    
    # ÜHENDA SLAID ÜLEJÄÄNUD ESITLUSEGA
    body.append(page)