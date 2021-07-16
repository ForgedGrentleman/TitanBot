from discord.ext import commands
import discord
import json

class Miscellaneous(commands.Cog):
	"""Miscellaneous commands that exist for no particular reason."""

	@commands.command(name='stab')
	async def stab(self, ctx, *stabbable: str):
		"""Stab someone, or something."""
		if str(stabbable) == "()":
			response = "Well, are you going to stab someone or not?"
		elif "(''," in str(stabbable).translate({ord(i): None for i in '*'}):
			response = "Try again when you can coherently form a word."
		elif "<@!865380885649031178>" in str('{}'.format(' '.join(stabbable).replace('*', ''))):
			response = "*" + str(ctx.message.author.mention) + " was shot by " + str(ctx.bot.user.mention) + "*"
		elif "<@!417794810284474378>" in str('{}'.format(' '.join(stabbable).replace('*', ''))) or "<@!509490815236833280>" in str('{}'.format(' '.join(stabbable).replace('*', ''))) or "<@!567446167827513350>" in str('{}'.format(' '.join(stabbable).replace('*', ''))):
			response = "*" + str(ctx.bot.user.mention) + " intervened and shot " + str('{}'.format(' '.join(stabbable).replace('*', ''))) + "*"
		else:
			response = "*" + str('{}'.format(' '.join(stabbable).replace('*', ''))) + " was stabbed by " + str(ctx.message.author.mention) + "*".lstrip(" ")
		await ctx.send(response)

	@commands.command(name='rock')
	async def rock(self, ctx, *rockable: str):
		"""Throw a rock at someone, or something."""
		if str(rockable) == "()":
			response = "Well, are you going to crush someone or not?"
		elif "(''," in str(rockable).translate({ord(i): None for i in '*'}):
			response = "Try again when you can coherently form a word."
		elif "<@!865380885649031178>" in str('{}'.format(' '.join(rockable).replace('*', ''))):
			response = "*" + str(ctx.message.author.mention) + " was shot by " + str(ctx.bot.user.mention) + "*"
		elif "<@!417794810284474378>" in str('{}'.format(' '.join(rockable).replace('*', ''))) or "<@!509490815236833280>" in str('{}'.format(' '.join(rockable).replace('*', ''))) or "<@!567446167827513350>" in str('{}'.format(' '.join(rockable).replace('*', ''))):
			response = "*" + str(ctx.bot.user.mention) + " intervened and shot " + str('{}'.format(' '.join(rockable).replace('*', ''))) + "*"
		else:
			response = "*" + str('{}'.format(' '.join(rockable).replace('*', ''))) + " was crushed with rocks by " + str(ctx.message.author.mention) + "*".lstrip(" ")
		await ctx.send(response)

	@commands.command(name='quote')
	async def quote(self, ctx, ID: int):
		"""Get a quote by number."""
		if ID != 0:
			with open('quote_list.json', 'r') as f:
				data = json.load(f)
				maxIndex = 0
				for i in data:
					maxIndex = maxIndex + 1
				if ID - 1 < maxIndex:
					response = "> " + data[ID - 1]["content"] + " - " + data[ID - 1]["author"]
				else:
					response = "You've given me a quote number higher than the number of quotes I have."
			
		else:
			response = "You can't have a quote number of zero."
		
		await ctx.send(response)

	@commands.command(name='addquote')
	@commands.guild_only()
	async def addquote(self, ctx, author: str, *quote: str):
		"""Someone said something stupid? Make them remember it by quoting them."""

		with open('quote_list.json', 'r') as f:
			data = json.load(f)
		
		with open('quote_list.json', 'w') as f:
			quoteDictionary = {"content": str('{}'.format(' '.join(quote))) , "author": str(author)}
			data = list(data)
			data.append(quoteDictionary)
			json.dump(data, f, indent=4)
		
		response = "Added quote to archive."
		
		await ctx.send(response)

	@commands.command(name='removequote')
	@commands.guild_only()
	async def removequote(self, ctx, ID: int):
		"""Remove a quote from the archive."""

		role = discord.utils.get(ctx.guild.roles, id=865619566334574603)
		if role in ctx.message.author.roles:
			with open('quote_list.json', 'r') as f:
				data = json.load(f)
				modifiedData = list(data)
				maxIndex = 0
				for i in data:
					maxIndex = maxIndex + 1
				if ID - 1 < maxIndex:
					modifiedData.remove(data[ID - 1])
					flag = True
				else:
					response = "You've given me a quote number higher than the number of quotes I have."
					flag = False

			with open('quote_list.json', 'w') as f:
				if flag == True:
					json.dump(modifiedData, f, indent=4)
					response = "Removed quote from archive."
		else:
			response = "You don't have the proper permissions for this action. Come back when you're more important."
		await ctx.send(response)