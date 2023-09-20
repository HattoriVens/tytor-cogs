import disnake
from disnake.ext import commands

class ButtonsModeration(disnake.ui.View):
    def __init__(self, пользователь, bot, author):
        self.member = пользователь
        self.bot = bot
        self.author = author
        super().__init__(timeout=None)

    @disnake.ui.button(label="Заблокировать", style=disnake.ButtonStyle.grey, row=0)
    async def ban(self, button: disnake.ui.Button, interaction: disnake.Interaction):
        if self.author.id == interaction.author.id:
            view = disnake.ui.View()
            view.add_item(BansSelect(self.member, self.author))
            embed = disnake.Embed(title="Управление баном", color=0x2F3136)
            embed.description = f"{interaction.author.mention} Выберите на сколько дней хотите заблокировать пользователя {self.member.mention}"
            embed.set_thumbnail(url=interaction.author.avatar.url)
            await interaction.response.edit_message(view=view, embed=embed)
        else:
            return

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="activate", description="Взаимодействовать с пользователем")
    async def activate(self, interaction, пользователь: disnake.Member,
                       должность=commands.Param(choices=['Куратор', 'Модератор', 'Саппорт'])):
        if должность == 'Модератор':
            if interaction.author.id != 1128433684354170901:
                embed = disnake.Embed(
                    title=f"Взаимодействовать с пользователем - {пользователь.name}#{пользователь.discriminator}",
                    color=0x2F3136)
                embed.description = f"Воспользуйтесь кнопками ниже чтобы взаимодействовать с пользователем"
                embed.set_thumbnail(url=пользователь.avatar.url)
                embed.set_author(name="Панель управления модератора")
                await interaction.response.send_message(embed=embed,
                                                        view=ButtonsModeration(пользователь, self.bot, interaction.author))
            else:
                embed = disnake.Embed(title="Ошибка", color=0x2F3136)
                embed.description = f"{interaction.author.mention} убейся))), поднимишься до модератора - сможешь использовать"
                embed.set_thumbnail(url=interaction.author.display_avatar.url)
                return await interaction.response.send_message(embed=embed, ephemeral=True)
        elif должность == 'Куратора':
            embed = disnake.Embed(
                title=f"Взаимодействовать с пользователем - {пользователь.name}#{пользователь.discriminator}",
                color=0x2F3136)
            embed.description = f"Воспользуйтесь кнопками ниже чтобы взаимодействовать с пользователем"
            embed.set_thumbnail(url=пользователь.avatar.url)
            embed.set_author(name="Панель управления куратора")
            await interaction.response.send_message(embed=embed,
                                                    view=ButtonsKurator(пользователь, self.bot, interaction.author))


def setup(bot):
    bot.add_cog(Commands(bot))