from discord import Client, Message, Game, AllowedMentions, Guild, Status, TextChannel, File, Attachment
from requests import get, Response
from emoji import is_emoji
from random import choice
from io import BytesIO
from time import sleep
from PIL import Image

class Application:
    """Base principal do aplicativo 'Theriana do agoj'"""
    target_guild: int = int(1323154125180895344)
    target: int = int(1323154125180895349)

    @staticmethod
    async def speak(message: Message, delay: int, tc: TextChannel) -> None:
        """
        Envia uma mensagem em um canal específico definido
        :param message: A integração da mensagem no canal
        :param delay: A demora que a mensagem demorará para ser enviada
        :param tc: Integração do canal a ser enviadop
        :return: Não retorna nada.
        """

        try:
            # Veirificação da split
            split: str = message.content.split("->speak ")[1]

            # Simulação de digitando
            await tc.typing()
            sleep(int(delay))

            # Veirifica se há anexos a mensagem
            if message.attachments:
                await tc.send(content=Application.set_emojis(str(split)), file=Application.set_asset(attachment=message.attachments[0]))
                return
            else:
                await tc.send(content=Application.set_emojis(message.content.split("->speak ")[1]))
        except Exception as exc:
            # usar a Astraprint aqui no futuro
            print(exc)

        pass

    @staticmethod
    async def reply(message: Message, delay: int, tc: TextChannel) -> None:
        """
        Permite responder uma mensagem a partir de seu ID
        :param message: A integração da mensagem que contém o comando;
        :param delay: A demora do bot para responder o usuário;
        :param tc: A integração do canal de texto;
        :return: Não retorna nada;
        """

        # Em casos de ocorrer erro na execução
        try:
            # Execução dos split
            split_cr: list[str] = message.content.split("->reply")
            split_ic: list[str] = split_cr[1].split(" - ")
            # split_ic[0] O ID do canal
            # split_ic[1] O conteúdo da mensagem

            # Tenta procurar a mensagem no canal
            if tc.get_partial_message(int(split_ic[0])):
                sleep(int(delay))
                if message.attachments:
                    await tc.get_partial_message(int(split_ic[0])).reply(Application.set_emojis(str(split_ic[1])), file=Application.set_asset(attachment=message.attachments[0]))
                    return
                else:
                    await tc.get_partial_message(int(split_ic[0])).reply(Application.set_emojis(str(split_ic[1])))
                    return
            else:
                await message.reply("<:system_why:1331271697399283827> Não é possível acessar essa mensagem.")
                return
        except Exception as exc:
            # Adicionar o Astraprint aqui no futuro
            print(exc)

    @staticmethod
    async def react(message: Message, tc: TextChannel) -> None:
        """
        Coloca algum emoji em uma mensagem
        :param message: A mensagem que executou o comando
        :param tc: O canal onde a mensagem alvo está
        :return: Nenhum valor é retornado
        """

        # Evita erros
        try:
            # Execução dos split
            split_cr: list[str] = message.content.split("->react")
            split_ie: list[str] = split_cr[1].split(" - ")
            # split_ic[0] O ID do canal
            # split_ic[1] O emoji
            # Tenta procurar a mensagem no canal
            if tc.get_partial_message(int(split_ie[0])):
                if is_emoji(split_ie[1]):
                    await tc.get_partial_message(int(split_ie[0])).add_reaction(str(split_ie[1]))
                else:
                    await message.reply("<:system_why:1331271697399283827> Esse emoji não é valido.")
            else:
                await message.reply("<:system_why:1331271697399283827> Não é possível acessar essa mensagem.")
                return
        except Exception as exc:
            # implementar astraprint no futuro
            print(exc)
            return


    # -------------------------------------------------------------- Código de eventos --------------------------------------------------------------

    @staticmethod
    async def on_started(ctx: Client) -> None:
        """
        Chamada quando o bot inicializa com sucesso
        @param ctx: Utilizado para interagir com o cliente.
        @returns: Não retorna nenhum valor
        """

        # Inicializa a atividade no perfil do bot
        activity: Game = Game(name="AstraCore 2.5", platform="Xbox")

        # Define as atividades do bot
        await ctx.change_presence(activity=activity, status=Status.idle)

        # Diz a quais menções a bot deve responder
        ctx.allowed_mentions = AllowedMentions(everyone=False, roles=False)
        pass

    @staticmethod
    async def message_reviced(message: Message, ctx: Client) -> None:
        """
        Chamada quando o bot detecta uma mensagem em um determinado canal
        :param ctx: O cliente do bot em execução.
        :param message: A instância da mensagem recebida.
        @return: Não retorna nenhum valor.
        """

        # Variaveis padrão
        target_server: Guild = ctx.get_guild(Application.target_guild)
        target_channel: TextChannel = target_server.get_channel(Application.target)
        commands_channel: TextChannel = target_server.get_channel(1331400582388252703)
        wait: int = choice([1, 2, 3])

        # Determina se a mensagem é no canal de comandos
        if not ctx.application_id == message.author.id:

            # Envia uma mensagem com o id
            await commands_channel.send(content=f"<:system_why:1331271697399283827> | ID de mensagem\n\n🤍 Mensagem:\n```{message.content}```\n🤍 ID da mensagem:\n```{message.id}```")
            await commands_channel.send(content="🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍🤍 ")

            if not str(message.channel.type) == "private":
                if int(message.channel.id) == int(1331234860131680316):
                    if not str("@everyone") in message.content or str("@here") in message.content:
                        # Comando de falar
                        if bool(message.content.startswith("->speak")):
                            await Application.speak(message=message, delay=int(wait), tc=target_channel)
                        elif bool(message.content.startswith("->reply")):
                            await Application.reply(message=message, delay=int(wait), tc=target_channel)
                        elif bool(message.content.startswith("->react")):
                            await Application.react(message=message, tc=target_channel)
                        else:
                            await message.reply("<:system_why:1331271697399283827> Não é possível encontrar a referência a um comando.")
                    else:
                        await message.reply("<:system_why:1331271697399283827> Por restrições do servidor, não é possível mencionar everyone e nem here.")
                        return
                else:
                    return
            else:
                return
        else:
            return

    # -------------------------------------------------------------- Funções do sistema --------------------------------------------------------------

    @staticmethod
    def set_asset(attachment: Attachment) -> File:
        """
        Baixa um determinado attachment (imagem) do Discord e envia parao bot
        :param attachment: A integração do attachment
        :return: Retorna a imagem em bytes.
        """
        try:
            attach: Response = get(url=str(attachment.url), stream=bool(True), allow_redirects=bool(False))
            attach.raise_for_status()

            image = Image.open(BytesIO(attach.content))

            with BytesIO() as image_binary:
                image.save(image_binary, 'PNG')
                image_binary.seek(0)

                # Escolhe o nome do arquivo
                fileNumbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                fileNumber: str = str("")
                fileNumberAddict: int = 15

                while int(fileNumberAddict) != 0:
                    fileNumber = str(f"{str(fileNumber)}{str(choice(fileNumbers))}")
                    fileNumberAddict = fileNumberAddict - 1

                file = File(fp=image_binary, filename=f"{str(fileNumberAddict)}-{attachment.filename}")
            return file
        except Exception as exc:
            # Implementar astraprint
            print(exc)

    @staticmethod
    def set_emojis(parse: str) -> str:
        parse = parse.replace("@furry1", "<:furry_one:1331271991583314083>")
        parse = parse.replace("@furry2", "<:furry_two:1331354153754165298>")
        parse = parse.replace("@furry3", "<:furry_three:1331385766571544647>")
        parse = parse.replace("@furry4", "<:furry_four:1331386026412740681>")
        parse = parse.replace("@furry5", "<:furry_five:1331388097069318214>")
        parse = parse.replace("@furry6", "<:furry_six:1331388582547554345>")
        return str(parse)