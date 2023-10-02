from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown


class MenuApp(App):

    def build(self):
        layout = BoxLayout(orientation='vertical')
        menu_bar = BoxLayout(size_hint=(1, None), height=50)

        # Criar um rótulo para o título do aplicativo
        title_label = Label(text='Sga Menu', size_hint=(None, None), size=(200, 50))
        menu_bar.add_widget(title_label)

        # Criar botão "Abrir" e associar uma ação a ele
        open_button = Button(text='Abrir')
        open_button.bind(on_release=self.show_open_popup)
        menu_bar.add_widget(open_button)

        # Criar botão "Salvar" e associar uma ação a ele
        save_button = Button(text='Salvar')
        save_button.bind(on_release=self.show_save_popup)
        menu_bar.add_widget(save_button)

        # Criar um botão "Sair" para sair do aplicativo
        exit_button = Button(text='Sair')
        exit_button.bind(on_release=self.stop)
        menu_bar.add_widget(exit_button)

        layout.add_widget(menu_bar)

        self.popup = None  # Variável para armazenar a janela pop-up aberta
        return layout

    def show_open_popup(self, instance):
        # Criar uma janela pop-up para a funcionalidade "Abrir"
        content = FileChooserListView()
        self.popup = Popup(title="Abrir Arquivo", content=content, size_hint=(0.9, 0.9))
        content.bind(on_selection=self.load_file)
        self.popup.open()

    def load_file(self, instance, value):
        # Manipule o arquivo selecionado aqui (por exemplo, abra-o)
        selected_file = value[0]
        with open(selected_file, 'r') as file:
            file_content = file.read()
        # Exiba o conteúdo do arquivo, mas você pode fazer o que quiser com ele
        print(f"Conteúdo do arquivo:\n{file_content}")
        self.popup.dismiss()

    def show_save_popup(self, instance):
        # Criar uma janela pop-up para a funcionalidade "Salvar"
        content = TextInput()
        self.popup = Popup(title="Salvar Arquivo", content=content, size_hint=(0.9, 0.9))
        save_button = Button(text="Salvar")
        save_button.bind(on_release=lambda x: self.save_file(content.text))
        self.popup.content.add_widget(save_button)
        self.popup.open()

    def save_file(self, content):
        # Manipule o conteúdo que você deseja salvar aqui
        # Neste exemplo, apenas exibimos o conteúdo
        print(f"Conteúdo a ser salvo:\n{content}")
        self.popup.dismiss()


if __name__ == '__main__':
    MenuApp().run()


