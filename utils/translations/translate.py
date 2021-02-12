# -*- coding: utf-8 -*-

import os
import json

from googletrans import Translator
from utils.logger import *

FILENAME = os.path.join(os.getcwd(), 'utils/translations/settings.json')


def gettex(message, input_language=None, output_language=None):
    try:
        with open(FILENAME) as jfile:
            settings = json.load(jfile)
            jfile.close()
    except Exception as ex:
        print(str(ex))
        logger.error('Error occurred '+str(ex))
    
    input_lang = input_language if input_language else settings['DEFAULT'].get('input')
    output_lang = output_language if output_language else settings['DEFAULT'].get('output')
    
    return CustomTranslator().translate(message, input_lang, output_lang)


class CustomTranslator:
    def __init__(self):

        self.translations = {}

    def __get_messages(self):
        try:
            with open(FILENAME) as jfile:
                self.translations = json.load(jfile)
                jfile.close()
        except Exception as ex:
            print(str(ex))
            logger.error('__get_messages:Error accurred: '+str(ex))
    
    def __set_messages(self, data):
        try:
            with open(FILENAME, 'w') as jfile:
                json.dump(data, jfile, indent=4)
                jfile.close()
        except Exception as ex:
            print(str(ex))
            logger.error('__set_messages:Error occurred: '+str(ex))
    
    @staticmethod
    def detect_language(message):
        try:
            lang = Translator().detect(message)
        except Exception as ex:
            print(str(ex))
            logger.error('detect_language:Error occurred: '+str(ex))
            return None
        
        return lang.lang
    
    @staticmethod
    def get_translation(message, output_lang):
        try:
            ret = Translator().translate(message, output_lang)
        except Exception as ex:
            print(str(ex))
            logger.error('get_translation:Error occurred: '+str(ex))
            return message
        
        return ret.text

    def translate(self, message, input_lang=None, output_lang=None):

        lang_message = self.detect_language(message)
        if not output_lang or not lang_message == input_lang or lang_message == output_lang:
            logger.warning('translate:Language not specified or output language equal to input language')
            return message
        
        self.__get_messages()

        has_update = False
        if not self.translations or not self.translations.get('LANGUAGES'):
            self.translations.update({
                'LANGUAGES': {
                    input_lang: {
                        message: {
                            output_lang: self.get_translation(message=message, output_lang=output_lang)
                        }
                    }
                }
            })
            has_update = True
        if not self.translations['LANGUAGES'].get(input_lang):
            self.translations['LANGUAGES'].update({
                input_lang: {
                    message: {
                        output_lang: self.get_translation(message=message, output_lang=output_lang)
                    }
                }
            })
            has_update = True
        if not self.translations['LANGUAGES'][input_lang].get(message):
            self.translations['LANGUAGES'][input_lang].update({
                message: {
                    output_lang: self.get_translation(message=message, output_lang=output_lang)
                }
            })
            has_update = True
        if not self.translations['LANGUAGES'][input_lang][message].get(output_lang):
            self.translations['LANGUAGES'][input_lang][message].update({
                output_lang: self.get_translation(message=message, output_lang=output_lang)
            })
            has_update = True

        try:
            trans_dict = self.translations['LANGUAGES']
            output_message = trans_dict[input_lang][message][output_lang]

            if has_update and not message == output_message:
                self.__set_messages(self.translations)
        except Exception as ex:
            print(str(ex))
            logger.error('translate:Error occurred: '+str(ex))
            output_message = message

        return output_message        
