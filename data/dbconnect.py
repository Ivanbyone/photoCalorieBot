""" """

import datetime

from typing import Any, Mapping
from motor.motor_asyncio import AsyncIOMotorClient

from config.config import DB_LINK


class MongoBase:

    # initializing connection to database and collections
    def __init__(self, db: str):
        self.client = AsyncIOMotorClient(db)
        self.database = self.client.get_database('calorie_Bot')
        self.users = self.database["users"]
        self.usersRequests = self.database["usersRequests"]
        self.payments = self.database["payments"]


    async def insert_user_to_base(self, tg_id: int, username: str, attempts: int, register_date: datetime, gender: str, age: str | int, weight: str | int, height: str | int, target: str, role="User") -> None:
        doc = {"telegramId": tg_id,
               "userName": username,
               "attempts": attempts,
               "registerDate": register_date,
               "role": role,
               "gender": gender,
               "age": age,
               "weight": weight,
               "height": height,
               "target": target,
               "recipesSubscribeEnd": None,
               "photoAttempts": None
               }
        await self.users.insert_one(doc)


    async def send_profile(self, tg_id: int) -> Mapping[str, Any] | None:
        profile = await self.users.find_one({"telegramId": tg_id})
        return profile


    async def change_gender(self, tg_id: int, gender: str):
        try:
            async with await self.client.start_session() as s:
                async with s.start_transaction():
                    await self.users.update_one({"telegramId": tg_id}, {"$set": {"gender": gender}})
                    new_gender = await self.users.aggregate([{"$match": {"telegramId": tg_id}}, {"$project": {"gender": "$gender"}}]).to_list(length=None)
                    return new_gender
        except Exception as e:
            print(e)


    async def change_age(self, tg_id: int, age: int):
        try:
            async with await self.client.start_session() as s:
                async with s.start_transaction():
                    await self.users.update_one({"telegramId": tg_id}, {"$set": {"age": age}})
                    new_age = await self.users.aggregate([{"$match": {"telegramId": tg_id}}, {"$project": {"age": "$age"}}]).to_list(length=None)
                    return new_age
        except Exception as e:
            print(e)


    async def change_weight(self, tg_id: int, weight: int):
        try:
            async with await self.client.start_session() as s:
                async with s.start_transaction():
                    await self.users.update_one({"telegramId": tg_id}, {"$set": {"weight": weight}})
                    new_weight = await self.users.aggregate([{"$match": {"telegramId": tg_id}}, {"$project": {"weight": "$weight"}}]).to_list(length=None)
                    return new_weight
        except Exception as e:
            print(e)


    async def change_height(self, tg_id: int, height: int):
        try:
            async with await self.client.start_session() as s:
                async with s.start_transaction():
                    await self.users.update_one({"telegramId": tg_id}, {"$set": {"height": height}})
                    new_height = await self.users.aggregate([{"$match": {"telegramId": tg_id}}, {"$project": {"height": "$height"}}]).to_list(length=None)
                    return new_height
        except Exception as e:
            print(e)


    async def change_target(self, tg_id: int, target: str):
        try:
            async with await self.client.start_session() as s:
                async with s.start_transaction():
                    await self.users.update_one({"telegramId": tg_id}, {"$set": {"target": target}})
                    new_target = await self.users.aggregate([{"$match": {"telegramId": tg_id}}, {"$project": {"target": "$target"}}]).to_list(length=None)
                    return new_target
        except Exception as e:
            print(e)


    async def save_photo_url(self, dateRequest: datetime,  tg_id: int, url: str):
        doc = {
            "telegramId": tg_id,
            "dateRequest": dateRequest,
            "photoUrl": url
        }
        await self.usersRequests.insert_one(doc)

    async def save_recipe_payment(self, tg_id: int, username: str, transaction: Any):
        doc = {
            "telegramId": tg_id,
            "username": username,
            "tag": "recipes",
            "paymentDate": datetime.datetime.utcnow().isoformat(),
            "transactionId": transaction
        }
        try:
            async with await self.client.start_session() as s:
                async with s.start_transaction():
                    await self.payments.insert_one(doc)
                    await self.users.update_one({"telegramId": tg_id}, {"$set": {"recipesSubscribeEnd": datetime.datetime.utcnow() + datetime.timedelta(days=180)}})
                    return { "all": "good"}
        except Exception as e:
            print(e)

    async def check_recipe_subscription(self, tg_id: int):
        profile = await self.users.find_one({"telegramId": tg_id})
        if profile['recipesSubscribeEnd'] == "None":
            return None
        else:
            date = profile['recipesSubscribeEnd']
            return date


    async def save_photo_payment(self, tg_id: int, username: str, transaction: Any, attempts: int):
        doc = {
            "telegramId": tg_id,
            "username": username,
            "tag": "photos",
            "paymentDate": datetime.datetime.utcnow().isoformat(),
            "transactionId": transaction
        }
        try:
            async with await self.client.start_session() as s:
                async with s.start_transaction():
                    await self.payments.insert_one(doc)
                    await self.users.update_one({"telegramId": tg_id}, {"$set": {"photoAttempts": attempts}})
                    return { "all": "good"}
        except Exception as e:
            print(e)

    async def check_photo_attempts(self, tg_id: int):
        profile = await self.users.find_one({"telegramId": tg_id})
        if profile['photoAttempts'] == "None":
            return None
        else:
            attempts = profile['photoAttempts']
            return attempts

    async def update_attempts(self, tg_id: int):
        await self.users.update_one(
            {"telegramId": tg_id}, {"$inc": {"photoAttempts": -1}}
        )


mongoBase = MongoBase(db=DB_LINK)
