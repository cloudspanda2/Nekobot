from discordrpc import presence

class Runtime:
    """Classe que permite e armazena o uso assíncrono de ações"""
    interaction: int = int(1330959463460372633)

    @staticmethod
    async def profile_presence() -> None:
        """Ativa a Rich Presence no perfil de quem está executando o bot localmente"""
        ctx = presence.RPC(app_id=int(Runtime.interaction))

        ctx.set_activity(
            state="🤍AstraCore AI",
            details="🤍 Aplicativo inicializado 🤍",

            # interação
            party_id="ae488379-351d-4a4f-ad32-2b9b051c91657",
            join_secret="MTI4NzM0OjFpMmhuZToxMjMxMjM=",
            party_size=[4, 5],

            # Imagem grande
            large_text="AstraCore 2.5",
            large_image="logotipo do bot",

            # Imagem pequena
            small_text="Astra Based AI",
            small_image="pequeno"

        )

        ctx.run(update_every=50)
        pass

    pass