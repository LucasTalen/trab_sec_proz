import aspose.pdf as ap



def emitir_certificado(nome = ''):
    document = ap.Document("certificado_aluno.pdf")
    stamp = ap.TextStamp(f"{nome}")
    stamp.x_indent = 200
    stamp.y_indent = 240
    stamp.background = False
    stamp.text_state.font = ap.text.FontRepository.find_font("Arial")
    stamp.text_state.font_size = 32
    stamp.text_state.foreground_color = ap.Color.black
    stamp.opacity = 100
    document.pages[1].add_stamp(stamp)
   
    
    document.save(f"./certificado_{nome}.pdf")

# emitir_certificado("Samuel Lucas Moura Macário")