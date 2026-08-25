from pathlib import Path

path = Path("main.lua")
text = path.read_text(encoding="utf-8")

old_draw = '''function GoldCompat.drawGoldTrainerSwitchOverlay(state)\n  local tr=state and state.__gen3uiTrainerSwitch\n  if not (tr and state.enemyTrainerImage) then return false end\n'''
new_draw = '''function GoldCompat.cbeOwnsEnemyTrainer(state)\n  if not (state and state.battle and not state.battle.wild) then return false end\n  if not (modRef and type(modRef.find)=="function") then return false end\n  local ok,handle=pcall(modRef.find,"COLOSSEUM_BATTLE_ENVIRONMENTS")\n  if not ok or not handle then\n    ok,handle=pcall(modRef.find,modRef,"COLOSSEUM_BATTLE_ENVIRONMENTS")\n  end\n  if not (ok and handle and type(handle.exports)=="table"\n      and type(handle.exports.status)=="function") then return false end\n  local statusOk,status=pcall(handle.exports.status)\n  if not (statusOk and type(status)=="table") then return false end\n  local trainer=status.trainer\n  return type(trainer)=="table" and trainer.active==true\nend\n\nfunction GoldCompat.drawGoldTrainerSwitchOverlay(state)\n  -- CBE already owns native trainer-picture suppression when its 3D enemy\n  -- actor is live. Do not bypass that contract by redrawing Gold's raw\n  -- trainer frontpic during the KO/replacement handoff.\n  if GoldCompat.cbeOwnsEnemyTrainer(state) then\n    if state then state.__gen3uiTrainerSwitch=nil end\n    return false\n  end\n  local tr=state and state.__gen3uiTrainerSwitch\n  if not (tr and state.enemyTrainerImage) then return false end\n'''
if text.count(old_draw) != 1:
    raise SystemExit(f"draw trainer switch anchor count={text.count(old_draw)}")
text = text.replace(old_draw, new_draw, 1)

old_offer = '''  GoldBattleState.offerShiftSwitch=function(self,mon,...)\n    self.__gen3uiTrainerSwitch={mode="in",frame=0}\n    return GoldBattleState.__gen3uiOriginalOfferShiftSwitch(self,mon,...)\n  end\n'''
new_offer = '''  GoldBattleState.offerShiftSwitch=function(self,mon,...)\n    -- Keep the stock Gold trainer-switch flourish only when no external 3D\n    -- trainer provider owns the enemy actor. CBE's live trainer must remain\n    -- authoritative through lethal damage, the shift prompt and send-out.\n    if GoldCompat.cbeOwnsEnemyTrainer(self) then\n      self.__gen3uiTrainerSwitch=nil\n    else\n      self.__gen3uiTrainerSwitch={mode="in",frame=0}\n    end\n    return GoldBattleState.__gen3uiOriginalOfferShiftSwitch(self,mon,...)\n  end\n'''
if text.count(old_offer) != 1:
    raise SystemExit(f"offer shift anchor count={text.count(old_offer)}")
text = text.replace(old_offer, new_offer, 1)

path.write_text(text, encoding="utf-8", newline="\n")
