import json, os
class ThemeManager:
    default_theme = 'Purple'
    color_presets = {
        'Purple': ('#9B59B6', '#8E44AD'),
        'Blue': ('#3498DB', '#2980B9'),
        'Green': ('#27AE60', '#1F8047'),
        'Red': ('#E74C3C', '#C0392B'),
        'Teal': ('#16A085', '#1F7A61'),
        'Orange': ('#D35400', '#C13A00'),
    }

    #default settings
    primary_color = '#9B59B6'
    hover_color = '#8E44AD' 
    current_theme = 'Purple'

    @classmethod
    def set_colors(cls, theme):
        cls.primary_color, cls.hover_color = cls.color_presets[theme]
        cls.current_theme = theme
        print(cls.primary_color, cls.hover_color)
        cls.save_theme()

    @classmethod
    def get_primary_color(cls):
        return cls.primary_color

    @classmethod
    def get_hover_color(cls):
        return cls.hover_color
    
    @classmethod
    def load_theme(cls):
        try:
            with open('settings.json', 'r') as file:
                settings = json.load(file)
                cls.current_theme = settings.get('current_theme', cls.current_theme)
                cls.set_colors(cls.current_theme)
            print(f'Theme settings loaded: {cls.current_theme}')
        except FileNotFoundError:
            print('Settings file not found. Using default theme.')
            cls.current_theme = cls.default_theme
            cls.set_colors(cls.current_theme)
            os.remove('settings.json')
        except Exception as e:
            print(f'Error loading theme from settings.json: {e}')

    @classmethod
    def save_theme(cls):
        settings = {
            'current_theme': cls.current_theme,
        }
        try:
            with open('settings.json', 'w') as file:
                json.dump(settings, file, indent=4)
            print('Theme settings saved successfully.')
        except Exception as e:
            print(f'Error saving theme to settings.json: {e}')

