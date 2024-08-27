from models import ChatSession, Conversation, Bot
from sqlalchemy.orm import Session
from domain.chat import chat_schema


def get_chat_session_histories(db: Session, user_id: int) -> list[ChatSession]:
    # 쿼리 작성 및 실행
    chat_sessions = db.query(ChatSession).filter(ChatSession.user_id == user_id).order_by(ChatSession.updated_at.desc()).all()
    return chat_sessions

def get_conversations(db: Session, chat_session_id: int):
    conversations = db.query(Conversation).filter(Conversation.chat_session_id == chat_session_id).order_by(Conversation.id.asc()).all()
    return conversations

def get_chat_session(db: Session, session_id: int):
    chat_session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
    return chat_session

def create_conversation(db: Session, conversation_create: chat_schema.ConversationCreate):
    chat_session = Conversation(chat_session_id=conversation_create.chat_session_id, 
                               sender=conversation_create.sender, 
                               message=conversation_create.message, 
                               sender_id = conversation_create.sender_id)
    db.add(chat_session)
    db.commit()

def create_chat_session(db: Session, chat_session_create: chat_schema.ChatSessionCreate):
    chat_session = ChatSession(user_id = chat_session_create.user_id,
                title = chat_session_create.title)
    db.add(chat_session)
    db.commit()
    return chat_session

def get_bot(db: Session, bot_id: int):
    bot = db.query(Bot).filter(Bot.id == bot_id).first()
    return bot