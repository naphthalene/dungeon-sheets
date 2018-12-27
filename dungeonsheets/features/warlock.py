from .features import (Feature, FeatureSelector)
from .. import spells, weapons


# Features
class EldritchInvocation(Feature):
    """In your study of occult lore, you have unearthed eldritch invocations,
    fragments of forbidden knowledge that imbue you with an abiding magical
    ability.

    At 2nd level, you gain two eldritch invocations of your choice. Your
    invocation options are detailed at the end of the class description. When
    you gain certain warlock levels, you gain additional invocations of your
    choice, as shown in the Invocations Known column of the Warlock table.

    Additionally, when you gain a level in this class, you can choose one of
    the invocations you know and replace it with another invocation that you
    could learn at that level.

    """
    name = "Eldritch Invocations"
    source = "Warlock"

    
class PactOfTheChain(Feature):
    """You learn the find familiar spell and can cast it as a ritual. The spell
    doesn’t count against your number of spells known.

    When you cast the spell, you can choose one of the normal forms for your
    familiar or one of the following special forms: imp, pseudodragon, quasit,
    or sprite. Additionally, when you take the Attack action, you can forgo one
    of your own attacks to allow your familiar to make one attack of its own.

    """
    name = "Pact of the Chain"
    source = "Warlock"
    spells_known = spells_prepared = (spells.FindFamiliar,)

    
class PactOfTheBlade(Feature):
    """You can use your action to create a pact weapon in your empty hand. You can
    choose the form that this melee weapon takes each time you create it (see
    chapter 5 for weapon options). You are proficient with it while you wield
    it. This weapon counts as magical for the purpose o f overcoming resistance
    and immunity to nonmagical attacks and damage.

    Your pact weapon disappears if it is more than 5 feet away from you for 1
    minute or more. It also disappears if you use this feature again, if you
    dismiss the weapon (no action required), or if you die.

    You can transform one magic weapon into your pact weapon by performing a
    special ritual while you hold the weapon. You perform the ritual over the
    course of 1 hour, which can be done during a short rest. You can then
    dismiss the weapon, shunting it into an extradimensional space, and it
    appears whenever you create your pact weapon thereafter. You can’t affect
    an artifact or a sentient weapon in this way. The weapon ceases being your
    pact weapon if you die, if you perform the 1-hour ritual on a different
    weapon, or if you use a 1-hour ritual to break your bond to it. The weapon
    appears at your feet if it is in the extradimensional space when the bond
    breaks.

    """
    name = "Pact of the Blade"
    source = "Warlock"


class PactOfTheTome(Feature):
    """Your patron gives you a grimoire called a Book of Shadows. When you gain
    this feature, choose three cantrips from any class’s spell list. While the
    book is on your person, you can cast those cantrips at will. They don’t
    count against your number of cantrips known.

    If you lose your Book of Shadows, you can perform a 1-hour ceremony to
    receive a replacement from your patron. This ceremony can be performed
    during a short or long rest, and it destroys the previous book. The book
    turns to ash when you die.

    """
    name = "Pact of the Tome"
    source = "Warlock"

    
class PactBoon(FeatureSelector):
    """Select a Pact Boon by choosing in feature_choices:

    pact of the chain

    pact of the blade
    
    pact of the tome

    """
    options = {'chain': PactOfTheChain,
               'pact of the chain': PactOfTheChain,
               'blade': PactOfTheBlade,
               'pact of the blade': PactOfTheBlade,
               'tome': PactOfTheTome,
               'pact of the tome': PactOfTheTome}
    name = "Pact Boon (Select One)"
    source = "Warlock"


class MysticArcanum(Feature):
    """At 11th level, your patron bestows upon you a magical secret called an
    arcanum. Choose one 6th-level spell from the warlock spell list as this
    arcanum.

    You can cast your arcanum spell once without expending a spell slot. You
    must finish a long rest before you can do so again.

    At higher levels, you gain more warlock spells of your choice that can be
    cast in this way: one 7th-level spell at 13th level, one 8th-level spell at
    15th level, and one 9th-level spell at 17th level. You regain all uses of
    your Mystic Arcanum when you finish a long rest.

    """
    name = "Mystic Arcanum"
    source = "Warlock"


class EldritchMaster(Feature):
    """At 20th level, you can draw on your inner reserve of mystical power while
    entreating your patron to regain expended spell slots. You can spend 1
    minute entreating your patron for aid to regain all your expended spell
    slots from your Pact Magic feature. Once you regain spell slots with this
    feature, you must finish a long rest before you can do so again.

    """
    name = "Eldritch Master"
    source = "Warlock"

    
# The Fiend Patron
class DarkOnesBlessing(Feature):
    """Starting at 1st level, when you reduce a hostile creature to 0 hit points,
    you gain temporary hit points equal to your Charisma modifier + your
    warlock level (minimum of 1)

    """
    _name = "Dark One's Blessing"
    source = "Warlock (The Fiend Patron)"

    @property
    def name(self):
        level = self.owner.Warlock.level
        mod = self.owner.charisma.modifier
        return self._name + ' ({:d} HP)'.format(level + mod)


class DarkOnesOwnLuck(Feature):
    """Starting at 6th level, you can call on your patron to alter fate in your
    favor. When you make an ability check or a saving throw, you can use this
    feature to add a d10 to your roll. You can do so after seeing the initial
    roll but before any o f the roll’s effects occur.

    Once you use this feature, you can’t use it again until you finish a short
    or long rest.

    """
    name = "Dark One's Own Luck"
    source = "Warlock (The Fiend Patron)"


class FiendishResilience(Feature):
    """Starting at 10th level, you can choose one damage type when you finish a
    short or long rest. You gain resistance to that damage type until you
    choose a different one with this feature. Damage from magical weapons or
    silver weapons ignores this resistance.

    """
    name = "Fiendish Resilience"
    source = "Warlock (The Fiend Patron)"


class HurlThroughHell(Feature):
    """Starting at 14th level, when you hit a creature with an attack, you can use
    this feature to instantly transport the target through the lower
    planes. The creature disappears and hurtles through a nightmare landscape.

    At the end of your next turn, the target returns to the space it previously
    occupied, or the nearest unoccupied space. If the target is not a fiend, it
    takes 10d10 psychic damage as it reels from its horrific experience.

    Once you use this feature, you can’t use it again until you finish a long
    rest.

    """
    name = "Hurl Through Hell"
    source = "Warlock (The Fiend Patron)"


# Hexblade
class HexbladesCurse(Feature):
    """Starting at lst level, you gain the ability to place a bale— ful curse on
    someone. As a bonus action, choose one creature you can see within 30 feet
    of you. The target is cursed for 1 minute. The curse ends early if the
    target dies, you die, or you are incapacitated. Until the curse ends, you
    gain the following benefits:

    -- You gain a bonus to damage rolls against the
    cursed target. The bonus equals your proficiency bonus.

    -- Any attack roll you make against the cursed target is a critical hit on
    a roll of 19 or 20 on the d20.

    --If the cursed target dies, you regain hit points equal to your warlock
    level + your Charisma modifier (mini- mum of 1 hit point).

    You can’t use this feature again until you finish a short or long rest.

    """
    name = "Hexblades Curse"
    source = "Warlock (Hexblade)"


class HexWarrior(Feature):
    """At lst level, you acquire the training necessary to effec- tively arm
    yourself for battle. You gain proficiency with medium armor, shields, and
    martial weapons.

    The influence of your patron also allows you to mystically channel your
    will through a particular weapon. Whenever you finish a long rest, you can
    touch one weapon that you are proficient with and that lacks the two-handed
    property. When you attack with that weapon, you can use your Charisma
    modifier, instead of Strength or Dexterity, for the attack and damage
    rolls. This benefit lasts until you finish a long rest. If you later gain
    the Pact of the Blade feature, this benefit extends to every pact weapon
    you conjure with that feature, no matter the weapon’s type

    """
    name = 'Hex Warrior'
    source = "Warlock (Hexblade)"

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        Swap the weapon's attack bonus modifier for Charisma if
        it is higher than STR/DEX bonus
        """
        if weapon.is_finesse:
            existing_mod = max(self.owner.strength.modifier,
                               self.owner.dexterity.modifier)
        else:
            existing_mod = self.owner.strength.modifier
        cha_mod = self.owner.charisma.modifier
        if cha_mod > existing_mod:
            weapon.attack_bonus += (cha_mod - existing_mod)
        return weapon

    
class AccursedSpecter(Feature):
    """Starting at 6th level, you can curse the soul of a person you slay,
    temporarily binding it to your service. When you slay a humanoid, you can
    cause its Spirit to rise from its corpse as a specter, the statistics for
    which are in the Monster Manual. When the specter appears, it gains
    temporary hit points equal to halfyour warlock level. Roll initiative for
    the specter, which has its own turns. It obeys your verbal commands, and it
    gains a special bonus to its attack rolls equal to your Charisma modifier
    (minimum of +0).

    The specter remains in your service until the end of your next long rest,
    at which point it vanishes to the afterlife.

    Once you bind a specter with this feature, you can’t use the feature again
    until you finish a long rest.

    """
    name = "Accursed Specter"
    source = "Warlock (Hexblade)"


class ArmorOfHexes(Feature):
    """At 10th level, your hex grows more powerful. If the tar- get cursed by your
    Hexblade’s Curse hits you with an attack roll, you can use your reaction to
    roll a d6. On a 4 or higher, the attack instead misses you, regardless of
    its roll.

    """
    name = "Armor of Hexes"
    source = "Warlock (Hexblade)"


class MasterOfHexes(Feature):
    """Starting at 14th level, you can spread your Hexblade’s Curse from a slain
    creature to another creature. When the creature cursed by your Hexblade’s
    Curse dies, you can apply the curse to a different creature you can see
    within 30 feet of you, provided you aren’t incapacitated. When you apply
    the curse in this way, you don’t regain hit points from the death of the
    previously cursed creature.

    """
    name = "Master of Hexes"
    source = "Warlock (Hexblade)"

    
# All Invocations
class Invocation(Feature):
    """
    A generic Eldritch Invocation. Add details in features/warlock.py
    """
    name = 'Unnamed Invocation'
    source = "Warlock (Eldritch Invocations)"
    at_will_spells = ()

    def cast_spell_at_will(self, spell):
        s = spell()
        s.level = 0
        if 'M' in s.components:
            c = list(s.components)
            c.remove('M')
            s.components = tuple(c)
        self.spells_known += (s,)
        self.spells_prepared += (s,)

    def __init__(self, owner):
        super().__init__(owner)
        for s in self.at_will_spells:
            self.cast_spell_at_will(s)


# PHB
class AgonizingBlast(Invocation):
    """When you cast eldritch blast, add your Charisma modifier to the damage it
    deals on a hit.

    """
    name = "Agonizing Blast"


class ArmorOfShadows(Invocation):
    """You can cast mage armor on yourself at will, without expending a spell slot
    or material components

    """
    name = "Armor of Shadows"
    at_will_spells = (spells.MageArmor,)


class AscendantStep(Invocation):
    """You can cast levitate on yourself at will, without expending a spell slot
    or material components.

    **Prerequisite: 9th level**

    """
    name = 'Ascendant Step'
    at_will_spells = (spells.Levitate,)


class BeastSpeech(Invocation):
    """You can cast speak with animals at will, without expending a spell slot.

    """
    name = "Beast Speech"
    at_will_spells = (spells.SpeakWithAnimals,)


class BeguilingInfluence(Invocation):
    """You gain proficiency in the Deception and Persuasion skills.

    """
    name = "Beguiling Influence"
    needs_implementation = True


class BewitchingWhispers(Invocation):
    """You can cast compulsion once using a warlock spell slot. You can’t do so
    again until you finish a long rest

    **Prerequisite**: 7th Level
    """
    name = "Bewitching Whispers"

    
class BookOfAncientSecrets(Invocation):
    """You can now inscribe magical rituals in your Book of Shadows. Choose two
    1st-level spells that have the ritual tag from any class’s spell list. The
    spells appear in the book and don’t count against the number of spells you
    know. With your Book of Shadows in hand, you can cast the chosen spells as
    rituals. You can’t cast the spells except as rituals, unless you’ve learned
    them by some other means. You can also cast a warlock spell you know as a
    ritual if it has the ritual tag.

    On your adventures, you can add other ritual spells to your Book o f
    Shadows. When you find such a spell, you can add it to the book if the
    spell’s level is equal to or less than half your warlock level (rounded up)
    and if you can spare the time to transcribe the spell. For each level of
    the spell, the transcription process takes 2 hours and costs 50 gp for the
    rare inks needed to inscribe it

    """
    name = "Book of Ancient Secrets"


class ChainsOfCarceri(Invocation):
    """You can cast hold monster at will—targeting a celestial, fiend, or
    elemental—without expending a spell slot or material components. You must
    finish a long rest before you can use this invocation on the same creature
    again.

    **Prerequisites**: 15th level, Pact of the Chain Feature
    """
    name = "Chains of Carceri"


class DevilsSight(Invocation):
    """You can see normally in darkness, both magical and nonmagical, to a
    distance of 120 feet.

    """
    name = "Devil's Sight"


class DreadfulWord(Invocation):
    """You can cast confusion once using a warlock spell slot. You can’t do so
    again until you finish a long rest.

    """
    name = "Dreadful Word"

    
class EldritchSight(Invocation):
    """You can cast detect magic at will, without expending a spell slot.

    """
    name = "Eldritch Sight"
    at_will_spells = (spells.DetectMagic,)


class EldritchSpear(Invocation):
    """When you cast eldritch blast, its range is 300 feet.

    """
    name = "Eldritch Spear"
    needs_implementation = True


class EyesOfTheRuneKeeper(Invocation):
    """
    You can read all writing.

    """
    name = "Eyes of the Rune Keeper"


class FiendishVigor(Invocation):
    """You can cast false life on yourself at will as a 1st-level spell, without
    expending a spell slot or material components.

    """
    name = "Fiendish Vigor"
    at_will_spells = (spells.FalseLife,)


class GazeOfTwoMinds(Invocation):
    """You can use your action to touch a willing humanoid and perceive through
    its senses until the end of your next turn. As long as the creature is on
    the same plane of existence as you, you can use your action on subsequent
    turns to maintain this connection, extending the duration until the end of
    your next turn. While perceiving through the other creature’s senses, you
    benefit from any special senses possessed by that creature, and you are
    blinded and deafened to your own surroundings.

    """
    name = "Gaze of Two Minds"


class LifeDrinker(Invocation):
    """When you hit a creature with your pact weapon, the creature takes extra
    necrotic damage equal to your Charisma modifier (minimum 1).
    
    **Prerequisite**: 12th Level, Pact of the Blade
    """
    name = "Life Drinker"
    needs_implementation = True


class MaskOfManyFaces(Invocation):
    """You can cast disguise self at will, without expending a spell slot.

    """
    name = "Mask of Many Faces"
    at_will_spells = (spells.DisguiseSelf,)


class MasterOfMyriadForms(Invocation):
    """
    You can cast alter self at will, without expending a spell slot.

    **Prerequisite**: 15th Level
    """
    name = "Master of Myriad Forms"
    at_will_spells = (spells.AlterSelf,)

    
class MinionsOfChaos(Invocation):
    """You can cast conjure elemental once using a warlock spell slot. You can’t
    do so again until you finish a long rest.

    **Prerequisite**: 9th Level
    """
    name = "Minions of Chaos"

    
class MireTheMind(Invocation):
    """You can cast slow once using a warlock spell slot. You can’t do so again
    until you finish a long rest.

    """
    name = "Mire the Mind"


class MistyVisions(Invocation):
    """You can cast silent image at will, without expending a spell slot or
    material components.

    """
    name = "Misty Visions"
    at_will_spells = (spells.SilentImage,)


class OneWithShadows(Invocation):
    """When you are in an area of dim light or darkness, you can use your action
    to become invisible until you move or take an action or a reaction.

    **Prerequisite**: 5th Level
    """
    name = "One with Shadows"


class OtherworldlyLeap(Invocation):
    """You can cast jump on yourself at will, without expending a spell slot or
    material components.

    **Prerequisite**: 9th Level

    """
    name = "Otherworldly Leap"
    at_will_spells = (spells.Jump,)


class RepellingBlast(Invocation):
    """When you hit a creature with eldritch blast, you can push the creature up
to 10 feet away from you in a straight line.

    """
    name = "Repelling Blast"


class SculptorOfFlesh(Invocation):
    """You can cast polymorph once using a warlock spell slot. You can’t do so
    again until you finish a long rest.

    **Prerequisite**: 7th Level
    """
    name = "Sculptor of Flesh"


class SignOfIllOmen(Invocation):
    """You can cast bestow curse once using a warlock spell slot. You can’t do so
    again until you finish a long rest.

    **Prerequisite**: 5th Level

    """
    name = "Sign of Ill Omen"

    
class ThiefOfFiveFates(Invocation):
    """You can cast bane once using a warlock spell slot. You can’t do so again
    until you finish a long rest.

    """
    name = "Thief of Five Fates"


class ThirstingBlade(Invocation):
    """You can attack with your pact weapon twice, instead of once, whenever you
    take the Attack action on your turn.
    
    **Prerequisite**: 5th Level, Pact of the Blade
    """
    name = "Thirsting Blade"


class VisionsOfDistantRealms(Invocation):
    """
    You can cast arcane eye at will, without expending a spell slot
    
    **Prerequisite**: 15th level
    """
    name = "Visions of Distant Realms"
    at_will_spells = (spells.ArcaneEye,)

    
class VoiceOfTheChain(Invocation):
    """You can communicate telepathically with your familiar and perceive through
    your familiar’s senses as long as you are on the same plane of
    existence. Additionally, while perceiving through your familiar’s senses,
    you can also speak through your familiar in your own voice, even if your
    familiar is normally incapable of speech.

    **Prerequisite**: Pact of the Chain

    """
    name = "Voice of the Chain"


class WhispersOfTheGrave(Invocation):
    """You can cast speak with dead at will, without expending a spell slot

    **Prerequsite**: 9th Level

    """
    name = "Whispers of the Grave"
    at_will_spells = (spells.SpeakWithDead,)


class WitchSight(Invocation):
    """You can see the true form of any shapechanger or creature concealed by
    illusion or transmutation magic while the creature is within 30 feet of you
    and within line of sight.

    """
    name = "Witch Sight"


# XGTE
class AspectOfTheMoon(Invocation):
    """You no longer need to sleep and can’t be forced to sleep by any means. To
    gain the benefits of a long rest, you can spend all 8 hours doing light
    activity, such as read- ing your Book of Shadows and keeping watch.

    **Prerequisite**: Pact of the Tome
    """
    name = "Aspect of the Moon"

    
class CloakOfFiles(Invocation):
    """As a bonus action, you can surround yourselfwith a magical aura that looks
    like buzzing flies. The aura ex- tends 5 feet from you in every direction,
    but not through total cover. It lasts until you’re incapacitated or you
    dismiss it as a bonus action.

    The aura grants you advantage on Charisma
    (Intimidation) checks but disadvantage on all other Charisma checks. Any
    other creature that starts its turn in the aura takes poison damage equal
    to your Charisma mod- ifier (minimum of O damage).

    Once you use this invocation, you can’t use it again until you finish a
    short or long rest.

    **Prerequisite**: 5th level
    """
    name = "Cloak of Flies"


class EldritchSmite(Invocation):
    """Once per turn when you hit a creature with your pact weapon, you can expend
    a warlock spell slot to deal an extra 1d8 force damage to the target, plus
    another 1d8 per level of the spell slot, and you can knock the target
    prone if it is Huge or smaller.

    **Prerequisite**: 5th level, Pact of the Blade

    """
    name = "Eldritch Smite"


class GhostlyGaze(Invocation):
    """As an action, you gain the ability to see through solid objects to a range
    of 30 feet. Within that range, you have darkvision if you don’t already
    have it. This special sight lasts for 1 minute or until your concentration
    ends (as if you were concentrating on a spell). During that time, you
    perceive objects as ghostly, transparent images.

    Once you use this invocation, you can’t use it again until you finish a
    short or long rest.

    **Prerequisite**: 7th level
    """
    name = "Ghostly Gaze"


class GiftOfTheDepths(Invocation):
    """You can breathe underwater, and you gain a swimming speed equal to your
    walking speed. You can also cast water breathing once without ex- pending a
    spell slot. You regain the ability to do so when you finish a long rest.

    **Prerequisite**: 5th level
    """
    name = "Gift of the Depths"
    
    
class GiftOfTheEverLivingOnes(Invocation):
    """Whenever you regain hit points while your familiar is within 100 feet
    ofyou, treat any dice rolled to determine the hit points you regain as
    having rolled their maxi- mum value for you.

    **Prerequisite**: Pact of the Chain
    """
    name = "Gift of the Ever-Living Ones"


class GraspOfHadar(Invocation):
    """Once on each ofyour turns when you hit a creature with your eldritcli
    blast, you can move that creature in a straight line 10 feet closer to you

    """
    name = "Grasp of Hadar"


class ImprovedPactWeapon(Invocation):
    """You can use any weapon you summon with your Pact of the Blade feature as a
    spellcasting focus for your waru lock spells.

    In addition, the weapon gains a +1 bonus to its attack and damage rolls,
    unless it is a magic weapon that already has a bonus to those rolls.

    Finally, the weapon you conjure can be a shortbow, longbow, light crossbow,
    or heavy crossbow.

    **Prerequisite**: Pact of the Blade
    """
    name = "Improved Pact Weapon"

    def weapon_func(self, weapon: weapons.Weapon, **kwargs):
        """
        Add +1 to attack and damage if magic is not already magic
        """
        if weapon.magic_bonus <= 1:
            weapon.magic_bonus = 1
            weapon.attack_bonus += 1
            weapon.bonus_damage += 1
        return weapon


class LanceOfLethargy(Invocation):
    """Once on each of your turns when you hit a creature with your eldritch
    blast, you can reduce that creature’s speed by 10 feet until the end ofyour
    next turn.

    """
    name = "Lance of Lethargy"


class MaddeningHex(Invocation):
    """As a bonus action, you cause a psychic disturbance around the target cursed
    by your hex spell or by a warlock feature of yours, such as Hexblade’s
    Curse or Sign of Ill Omen. When you do so, you deal psychic damage to the
    cursed target and each creature of your choice that you can see within 5
    feet of it. The psychic damage equals your Charisma modifier (minimum of 1
    dam- age). To use this invocation, you must be able to see the cursed
    target, and it must be within 30 feet ofyou.

    **Prerequisite**: 5th level
    """
    name = "Maddening Hex"


class RelentlessHex(Invocation):
    """Your curse creates a temporary bond between you and your target. As a bonus
    action, you can magically telerport up to 30 feet to an unoccupied space
    you can see within 5 feet of the target cursed by your hex spell or by a
    warlock feature ofyours, such as Hexblade’s Curse or Sign of 111 Omen. To
    teleport in this way, you must be able to see the cursed target.

    """
    name = "Relentless Hex"


class ShroudOfShadow(Invocation):
    """You can cast invisibility at will, without expending a spell slot.

    **Prerequisite**: 15th Level

    """
    at_will_spells = (spells.Invisibility,)
    name = "Shroud of Shadow"


class TombOfLevistus(Invocation):
    """As a reaction when you take damage, you can entomb yourself in ice, which
    melts away at the end ofyour next turn. You gain 10 temporary hit points
    per warlock level, which take as much of the triggering damage as
    possible. Immediately after you take the damage, you gain vulnerability to
    fire damage, your speed is reduced to 0, and you are incapacitated. These
    effects, including any remaining temporary hit points, all end when the ice
    melts.

    Once you use this invocation, you can’t use it again until you finish a
    short or long rest.

    **Prerequisite**: 5th Level

    """
    name = "Tomb of Levistus"


class TrickstersEscape(Invocation):
    """You can cast freedom ofmovement once on yourself without expending a spell
    slot. You regain the ability to do so when you finish a long rest

    """
    name = "Tricksters Escape"
    
