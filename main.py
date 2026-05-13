import time
import platform
import threading
import webbrowser
from gtts import gTTS
from plyer import uniqueid
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRaisedButton


# Definição do layout em KV
KV = '''
ScreenManager:
    id: screen_manager
    initial: 'tela_inicial'
    TelaInicial:
    TelaPrograma:

<TelaInicial>:
    name: 'tela_inicial'
    FloatLayout:
        orientation: 'vertical'
        Image:
            source: 'fundo-inicial.png'
            allow_stretch: True
            keep_ratio: False
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: (1, 1)

        MDLabel:
            id: titulo_inicio
            text: "Tabuada com Áudio"
            font_style: 'H5'
            halign: 'center'
            size_hint_y: None
            height: dp(30)
            pos_hint: {'center_x': 0.5, 'top': 0.99}
            theme_text_color: 'Custom'
            text_color: 1, 1, 0, 1  # Cor da letra amarela
            secondary_text_color: 0, 0, 0, 1  # Cor da sombra preta

        MDLabel:
            text: "[b][color=0000FF]Select the Language[/color][/b]"
            markup: True
            pos_hint: {'center_y': 0.70}
            halign: 'center'
            
        MDLabel:
            text: "(Selecione o idioma)"
            pos_hint: { 'center_y': 0.65}
            halign: 'center'

        # Botão para gerar a tabuada
        MDRaisedButton:
            id: botao_por
            text: 'Português'
            on_press: root.idioma_por()
            pos_hint: {'center_x': 0.5, 'center_y': 0.57}
            size_hint_x: 0.35  # Defina a largura absoluta
            size_hint_y: 0.05  # Defina a altura  absoluta
            md_bg_color: 1, 1, 0, 1  # Fundo amarelo
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1  # Cor da letra preta

        MDRaisedButton:
            id: botao_eng
            text: ' English '
            on_press: root.idioma_eng()
            pos_hint: {'center_x': 0.5, 'center_y': 0.50}
            size_hint_x: 0.35  # Defina a largura absoluta
            size_hint_y: 0.05  # Defina a altura  absoluta
            md_bg_color: 1, 1, 0, 1  # Fundo amarelo
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1  # Cor da letra preta

        MDRaisedButton:
            id: botao_esp
            text: ' Español '
            on_press: root.idioma_esp()
            pos_hint: {'center_x': 0.5, 'center_y': 0.43}
            size_hint_x: 0.35  # Defina a largura absoluta
            size_hint_y: 0.05  # Defina a altura  absoluta
            md_bg_color: 1, 1, 0, 1  # Fundo amarelo
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1  # Cor da letra preta

        MDRaisedButton:
            id: botao_ita
            text: 'Italiano '
            on_press: root.idioma_ita()
            pos_hint: {'center_x': 0.5, 'center_y': 0.36}
            size_hint_x: 0.35  # Defina a largura absoluta
            size_hint_y: 0.05  # Defina a altura  absoluta
            md_bg_color: 1, 1, 0, 1  # Fundo amarelo
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1  # Cor da letra preta

        # Botão para sair do aplicativo
        MDRaisedButton:
            id: botao_sair_inicio
            text: '    Sair    '
            on_press: app.parar()
            pos_hint: {'center_x': 0.5, 'center_y': 0.15}
            size_hint_x: 0.35  # Defina a largura absoluta
            size_hint_y: 0.05  # Defina a altura  absoluta
            md_bg_color: 1, 0, 0, 1

        # Label com o site da BGMax Tecnologia
        MDLabel:
            text: "[ref=site][color=#FFFFFF]www.bgmax.com.br/tecnologia[/color][/ref]"
            markup: True
            halign: 'center'
            valign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.018}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto (branco)
            on_ref_press: app.open_link('www.bgmax.com.br/tecnologia')

            
<TelaPrograma>:
    name: 'tela_programa'
    FloatLayout:
        canvas.before:
            Color:
                rgba: 0, 0, 0, 1
            Rectangle:
                pos: self.pos
                size: self.size

        Image:
            source: 'fundo-tabuada.png'
            allow_stretch: True
            keep_ratio: False
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            size_hint: (1, 1)

        MDLabel:
            id: titulo
            text: "Tabuada com Áudio"
            font_style: 'H6'
            halign: 'center'
            size_hint_y: None
            height: dp(30)
            pos_hint: {'center_x': 0.5, 'top': 0.99}
            theme_text_color: 'Custom'
            text_color: 1, 1, 0, 1  # Cor da letra amarela
            secondary_text_color: 0, 0, 0, 1  # Cor da sombra preta

        # Campo de entrada para o número da tabuada
        MDTextField:
            id: numero_entrada
            hint_text: 'Digite o número da tabuada'
            input_type: 'number'
            helper_text_mode: 'on_focus'
            helper_text: 'Digite um número (1 a 10)'  # Adicionado limite de 1 a 10
            pos_hint: {'x': 0.05, 'y': 0.83}
            size_hint: (0.40, 0.1)
            theme_text_color: 'Primary'
            hint_text_color: 1, 1, 1, 1  # Cor do texto de sugestão (branco)

        # Botão para gerar a tabuada
        MDRaisedButton:
            id: botao_gerar
            text: 'Gerar'
            on_press: app.gerar_tabuada()
            pos_hint: {'x': 0.05, 'y': 0.75}
            size_hint: (0.34, 0.05)
            text_color: 0, 0, 0, 1
            md_bg_color: 1, 1, 0, 1

        # Área de rolagem para a lista da tabuada
        ScrollView:
            pos_hint: {'x': 0.05, 'y': 0.08}
            size_hint: (0.34, 0.67)
            MDList:
                id: lista_tabuada

        # Botão para falar
        MDRaisedButton:
            id: botao_falar
            text: 'Falar'
            on_press: app.audio()
            pos_hint: {'x': 0.02, 'center_y': 0.07}
            size_hint: (0.20, 0.04)
            disabled: True  # Inicialmente desabilitado

        # Botão para gerar nova tabuada
        MDRaisedButton:
            id: botao_nova
            text: 'Nova Tabuada'
            on_press: app.nova_tabuada()
            pos_hint: {'center_x': 0.38, 'center_y': 0.07}
            size_hint: (0.20, 0.04)
            md_bg_color: 1, 1, 0, 1
            theme_text_color: 'Custom'
            text_color: 0, 0, 0, 1
            disabled: True  # Inicialmente desabilitado

        # Botão para sair do aplicativo
        MDRaisedButton:
            id: botao_sel_idioma
            text: 'Idioma'
            on_press: app.sel_idioma()
            pos_hint: {'center_x': 0.63, 'center_y': 0.07 }
            size_hint: (0.20, 0.04)
            md_bg_color: 0.25, 0.88, 0.13, 1  # Verde grama
            text_color: 0, 0, 0, 1

        # Botão para sair do aplicativo
        MDRaisedButton:
            id: botao_sair
            text: '    Sair    '
            on_press: app.parar()
            pos_hint: {'center_x': 0.88, 'center_y': 0.07 }
            size_hint: (0.20, 0.04)
            md_bg_color: 1, 0, 0, 1
            
        # Label com o site da BGMax Tecnologia
        MDLabel:
            text: "[ref=site][color=#FFFFFF]www.bgmax.com.br/tecnologia[/color][/ref]"
            markup: True
            halign: 'center'
            valign: 'center'
            pos_hint: {'center_x': 0.5, 'center_y': 0.018}
            theme_text_color: "Custom"
            text_color: 1, 1, 1, 1  # Cor do texto (branco)
            on_ref_press: app.open_link('www.bgmax.com.br/tecnologia')
'''

class TelaInicial(Screen):
    def idioma_por(self):
        global idioma
        idioma = "Por"
        app = MDApp.get_running_app()
        app.root.current = 'tela_programa'
        app.title = "Tabuada com Áudio"
        app.root.get_screen('tela_programa').ids.titulo.text = app.title
        app.root.get_screen('tela_programa').ids.botao_gerar.text = 'Gerar'
        app.root.get_screen('tela_programa').ids.botao_falar.text = 'Falar'
        app.root.get_screen('tela_programa').ids.botao_nova.text = 'Nova'
        app.root.get_screen('tela_programa').ids.botao_sel_idioma.text = 'Idioma'
        app.root.get_screen('tela_programa').ids.botao_sair.text = 'Sair'
        app.root.get_screen('tela_programa').ids.numero_entrada.hint_text = 'Digite o número da tabuada'
        app.root.get_screen('tela_programa').ids.numero_entrada.helper_text = 'Digite um número (1 a 10)'

        
    def idioma_eng(self):
        global idioma
        idioma = "Eng"
        app = MDApp.get_running_app()
        app.root.current = 'tela_programa'
        app.title = "Times Table with Audio"
        app.root.get_screen('tela_programa').ids.titulo.text = app.title
        app.root.get_screen('tela_programa').ids.botao_gerar.text = 'Generate'
        app.root.get_screen('tela_programa').ids.botao_falar.text = 'Speak'
        app.root.get_screen('tela_programa').ids.botao_nova.text = 'New'
        app.root.get_screen('tela_programa').ids.botao_sel_idioma.text = 'Language'
        app.root.get_screen('tela_programa').ids.botao_sair.text = 'Exit'
        app.root.get_screen('tela_programa').ids.numero_entrada.hint_text = 'Enter the multiplication number'
        app.root.get_screen('tela_programa').ids.numero_entrada.helper_text = 'Enter a number (1 to 10)'
        
    def idioma_esp(self):
        global idioma
        idioma = "Esp"
        app = MDApp.get_running_app()
        app.root.current = 'tela_programa'
        app.title= 'Tabla de Multiplicación con Audio'
        app.root.get_screen('tela_programa').ids.titulo.text = app.title
        app.root.get_screen('tela_programa').ids.botao_gerar.text = 'Generar'
        app.root.get_screen('tela_programa').ids.botao_falar.text = 'Falar'
        app.root.get_screen('tela_programa').ids.botao_nova.text = 'Nuevo'
        app.root.get_screen('tela_programa').ids.botao_sel_idioma.text = 'Idioma'
        app.root.get_screen('tela_programa').ids.botao_sair.text = 'Salir'
        app.root.get_screen('tela_programa').ids.numero_entrada.hint_text = 'Ingrese el número de multiplicación'
        app.root.get_screen('tela_programa').ids.numero_entrada.helper_text = 'Ingrese un número (1 a 10)'

    def idioma_ita(self):
        global idioma
        idioma = "Ita"
        app = MDApp.get_running_app()
        app.root.current = 'tela_programa'
        app.title= "Tabelline con Audio"
        app.root.get_screen('tela_programa').ids.titulo.text = app.title
        app.root.get_screen('tela_programa').ids.botao_gerar.text = 'Generare'
        app.root.get_screen('tela_programa').ids.botao_falar.text = 'Parlare'
        app.root.get_screen('tela_programa').ids.botao_nova.text = 'Uscire'
        app.root.get_screen('tela_programa').ids.botao_sel_idioma.text = 'Lingua'
        app.root.get_screen('tela_programa').ids.botao_sair.text = 'Salir'
        app.root.get_screen('tela_programa').ids.numero_entrada.hint_text = 'Inserisci il numero della tabellina'
        app.root.get_screen('tela_programa').ids.numero_entrada.helper_text = 'Inserisci un numero (1 a 10)'


class TelaPrograma(Screen):
    pass

class TabuadaApp(MDApp):
    #Armazenar dados do dispositivo
##    def dados_dispostivo(self):
##        device_id = uniqueid.id
##        con=conexao.conexao()
##        self.som = None
##        try:
##            sql_text = f"insert into ctrl_tabuada (device_id) values ('{device_id}')"
##            con.gravar(sql_text)
##            con.fechar()
##        except:
##            pass
##        finally:
##            pass
        
    def build(self):
        self.title = "Tabuada com Áudio"
        sistema = platform.system()
        if sistema == 'Windows':
            # Configura a tela para um tamanho específico em sistemas Windows
            Window.size = (720/2, 1280/2)
            
            

        #self.dados_dispostivo()
        
        return Builder.load_string(KV)
    

   # Voltar para tela de seleção do idioma
    def sel_idioma(self):
        app = MDApp.get_running_app()
        app.root.current = 'tela_inicial'
   
   # Método para iniciar nova tabuada
    def nova_tabuada(self):
        self.root.get_screen('tela_programa').ids.numero_entrada.text = ''
        self.root.get_screen('tela_programa').ids.botao_falar.disabled = True  # Desabilita o botão falar
        self.root.get_screen('tela_programa').ids.botao_nova.disabled = True  # Desabilita o botão após pressionamento
         
        lista_tabuada = self.root.get_screen('tela_programa').ids.lista_tabuada
        lista_tabuada.clear_widgets()

    def parar(self):
        if self.som:
            self.som.stop()
        MDApp.get_running_app().stop()


    # Método para reproduzir áudio da tabuada
    def reproduzir_audio_thread(self):
        self.root.get_screen('tela_programa').ids.botao_falar.disabled = True           # Desabilita o botão após pressionamento
        self.root.get_screen('tela_programa').ids.botao_nova.disabled = True            # Desabilita o botão após pressionamento
        self.root.get_screen('tela_programa').ids.botao_sel_idioma.disabled = True      # Desabilita o botão após pressionamento
        
        try:
            for i in range(1, 11):
                if idioma == "Por":
                    texto_audio = f"{self.numero} vezes {i} igual a {self.numero * i}, "
                    tts = gTTS(text=texto_audio, lang="pt-br", slow=False)
                elif idioma == "Eng":
                    texto_audio = f"{self.numero} times {i} is  {self.numero * i}, "
                    tts = gTTS(text=texto_audio, lang="en-US", slow=False)
                elif idioma == "Esp":
                    texto_audio = f"{self.numero} por {i}, {self.numero * i}, "
                    tts = gTTS(text=texto_audio, lang="es-ES", slow=False)
                elif idioma == "Ita":
                    texto_audio = f"{self.numero} per  {i} , {self.numero * i}, "
                    tts = gTTS(text=texto_audio, lang="it", slow=False)
                

                audio_seq = f"./{self.numero}.mp3"
                tts.save(audio_seq)

                self.som = SoundLoader.load(audio_seq)
                if self.som:
                    self.som.play()
                    time.sleep(3.2)
        except Exception as e:
            # Exceção ao reproduzir áudio
            mensagem_erro = "Não foi possível gerar e reproduzir o áudio.\n" \
                            "Favor verificar sua conexão com a internet."
            self.popup_internet("Conexão", mensagem_erro)

        self.root.get_screen('tela_programa').ids.botao_falar.disabled = False         # Habilita o botão falar
        self.root.get_screen('tela_programa').ids.botao_nova.disabled = False          # Habilita o botão nova tabuada
        self.root.get_screen('tela_programa').ids.botao_sel_idioma.disabled = False    # Habilita o botão idioma
       

    def audio(self):
        thread = threading.Thread(target=self.reproduzir_audio_thread)
        thread.start()

    def popup_internet(self, titulo, mensagem):
        conteudo = BoxLayout(orientation='vertical', padding=10, spacing=10)
        conteudo.add_widget(Label(text=mensagem, halign='center'))
        
        # Botão "Fechar" centralizado na horizontal
        btn_fechar = Button(text='Fechar', on_press=self.fechar_popup, size_hint=(None, None), size=(100, 30), halign='center')
        conteudo.add_widget(btn_fechar)

        popup = Popup(title=titulo, content=conteudo, size_hint=(None, None), size=(500, 180))
        popup.open()

        # Salvar uma referência ao popup para fechá-lo posteriormente, se necessário
        self.popup = popup

    def fechar_popup(self, instance):
        self.popup.dismiss()

    # Método para gerar a tabuada
    def gerar_tabuada(self):
        try:
            self.numero = int(self.root.get_screen('tela_programa').ids.numero_entrada.text)
            if 1 <= self.numero <= 10:
                pass
            else:
                self.root.get_screen('tela_programa').ids.numero_entrada.error = False
                self.root.get_screen('tela_programa').ids.numero_entrada.text = ''
                return
        except ValueError:
            self.root.get_screen('tela_programa').ids.numero_entrada.error = True
            return

        self.root.get_screen('tela_programa').ids.numero_entrada.error = False
        self.root.get_screen('tela_programa').ids.botao_falar.disabled = False       # Habilita o botão após a geração da tabuada
        self.root.get_screen('tela_programa').ids.botao_nova.disabled = False        # Habilita o botão após pressionamento
        self.root.get_screen('tela_programa').ids.botao_sel_idioma.disabled = False  # Habilita o botão idioma
        self.root.get_screen('tela_programa').ids.botao_sair.disabled = False        # Habilita o botão sair
        
        #self.texto_audio = ""

        lista_tabuada = self.root.get_screen('tela_programa').ids.lista_tabuada
        lista_tabuada.clear_widgets()

        for i in range(1, 11):
            texto_tabuada = f'{self.numero} x {i} = {self.numero * i}'

            botao_tabuada = MDRaisedButton(
                text=texto_tabuada[:20],
                size_hint=(50, 50)
            )

            lista_tabuada.add_widget(botao_tabuada)

    def open_link(self, link):
        webbrowser.open(f'http://{link}')


if __name__ == '__main__':
    TabuadaApp().run()
