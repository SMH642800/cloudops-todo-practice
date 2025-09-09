from pydantic import BaseModel

# 基礎欄位 (共用)
class TodoBase(BaseModel):
    title: str
    description: str | None = None

# 建立用
class TodoCreate(TodoBase):
    pass

# 更新用
class TodoUpdate(TodoBase):
    completed: bool

# 回傳用 (含 id)
class TodoResponse(TodoBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True