
import telebot

CHAVE_API= '8314548372:AAE6xCXn6oky77NnX92gin6eA2ypAYyDQyM'


bot = telebot.TeleBot(CHAVE_API)

@bot.message_handler(commands=["opcao1"])
def opcao1(mensagem):
    pass

@bot.message_handler(commands=["opcao2"])
def opcao2(mensagem):
    pass

@bot.message_handler(commands=["opcao3"])
def opcao3(mensagem):
    bot.reply_to(mensagem,"Ok, dentro de alguns minutos o gerente irá na sua mesa!")
    




def verificar(mensagem):
    return True

@bot.message_handler(func=verificar) #decorator criado junto com a função
def responder(mensagem): #função para ter uma resposta inicial ao utilizar o bot
    texto =""" 
    Olá, aqui é o bot do João!Escolha uma opção para continuar.(Clique no item):
        /opcao1 Fzer um pedido
        /opcao2 Ver Menu
        /opcao3 Reclamar de um pedido
        Responder qualquer coisa não irá funcionar, clique em uma das opções acima."""
    bot.reply_to(mensagem,texto)



bot.polling()
