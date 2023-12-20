"""empty message

Revision ID: f12c61cdbdf4
Revises: 
Create Date: 2023-12-20 13:12:01.133416

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f12c61cdbdf4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('category_disease',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_category_disease'))
    )
    op.create_table('client',
    sa.Column('date_birthday', sa.Date(), nullable=False),
    sa.Column('address', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('middle_name', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_client')),
    sa.UniqueConstraint('first_name', 'last_name', 'middle_name', name='uq_client_full_name')
    )
    op.create_table('profession',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_profession')),
    sa.UniqueConstraint('name', name=op.f('uq_profession_name'))
    )
    op.create_table('disease',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('category_disease_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['category_disease_id'], ['category_disease.id'], name=op.f('fk_disease_category_disease_id_category_disease')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_disease'))
    )
    op.create_index(op.f('ix_disease_category_disease_id'), 'disease', ['category_disease_id'], unique=False)
    op.create_table('doctor',
    sa.Column('date_start_work', sa.Date(), nullable=False),
    sa.Column('profession_id', sa.Integer(), nullable=True),
    sa.Column('first_name', sa.String(length=255), nullable=False),
    sa.Column('last_name', sa.String(length=255), nullable=False),
    sa.Column('middle_name', sa.String(length=255), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['profession_id'], ['profession.id'], name=op.f('fk_doctor_profession_id_profession'), ondelete='SET NULL'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_doctor')),
    sa.UniqueConstraint('first_name', 'last_name', 'middle_name', name='uq_doctor_names')
    )
    op.create_index(op.f('ix_doctor_profession_id'), 'doctor', ['profession_id'], unique=False)
    op.create_table('diagnosis',
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=1000), nullable=False),
    sa.Column('date_closed', sa.DateTime(), nullable=False),
    sa.Column('status', sa.Enum('ACTIVE', 'CLOSED', name='statuschoices'), nullable=False),
    sa.Column('client_id', sa.Integer(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], name=op.f('fk_diagnosis_client_id_client'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], name=op.f('fk_diagnosis_doctor_id_doctor'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_diagnosis'))
    )
    op.create_index(op.f('ix_diagnosis_client_id'), 'diagnosis', ['client_id'], unique=False)
    op.create_index(op.f('ix_diagnosis_doctor_id'), 'diagnosis', ['doctor_id'], unique=False)
    op.create_table('make_anappointment',
    sa.Column('start_date_appointment', sa.DateTime(), nullable=False),
    sa.Column('end_date_appointment', sa.DateTime(), nullable=False),
    sa.Column('doctor_id', sa.Integer(), nullable=True),
    sa.Column('client_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['client_id'], ['client.id'], name=op.f('fk_make_anappointment_client_id_client'), ondelete='SET NULl'),
    sa.ForeignKeyConstraint(['doctor_id'], ['doctor.id'], name=op.f('fk_make_anappointment_doctor_id_doctor'), ondelete='SET NULl'),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_make_anappointment'))
    )
    op.create_index(op.f('ix_make_anappointment_client_id'), 'make_anappointment', ['client_id'], unique=False)
    op.create_index(op.f('ix_make_anappointment_doctor_id'), 'make_anappointment', ['doctor_id'], unique=False)
    op.create_table('disease_diagnosis',
    sa.Column('disease_id', sa.Integer(), nullable=False),
    sa.Column('diagnosis_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['diagnosis_id'], ['diagnosis.id'], name=op.f('fk_disease_diagnosis_diagnosis_id_diagnosis'), ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['disease_id'], ['disease.id'], name=op.f('fk_disease_diagnosis_disease_id_disease'), ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('disease_id', 'diagnosis_id', 'id', name=op.f('pk_disease_diagnosis'))
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('disease_diagnosis')
    op.drop_index(op.f('ix_make_anappointment_doctor_id'), table_name='make_anappointment')
    op.drop_index(op.f('ix_make_anappointment_client_id'), table_name='make_anappointment')
    op.drop_table('make_anappointment')
    op.drop_index(op.f('ix_diagnosis_doctor_id'), table_name='diagnosis')
    op.drop_index(op.f('ix_diagnosis_client_id'), table_name='diagnosis')
    op.drop_table('diagnosis')
    op.drop_index(op.f('ix_doctor_profession_id'), table_name='doctor')
    op.drop_table('doctor')
    op.drop_index(op.f('ix_disease_category_disease_id'), table_name='disease')
    op.drop_table('disease')
    op.drop_table('profession')
    op.drop_table('client')
    op.drop_table('category_disease')
    # ### end Alembic commands ###