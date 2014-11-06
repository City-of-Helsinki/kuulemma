"""Create `image` table"""

# revision identifiers, used by Alembic.
revision = '51051f5b195'
down_revision = '32989394feb'

import sqlalchemy as sa
from alembic import op


def upgrade():
    op.create_table(
        'image',
        sa.Column(
            'id',
            sa.Integer(),
            nullable=False
        ),
        sa.Column(
            'created_at',
            sa.DateTime(),
            server_default='now()',
            nullable=False
        ),
        sa.Column(
            'updated_at',
            sa.DateTime(),
            nullable=True
        ),
        sa.Column(
            'hearing_id',
            sa.Integer()
        ),
        sa.Column(
            'hearing_section_id',
            sa.Integer(),
        ),
        sa.Column(
            'image_url',
            sa.Unicode(length=255),
            server_default='',
            nullable=False
        ),
        sa.Column(
            'caption',
            sa.UnicodeText(),
            server_default='',
            nullable=False
        ),
        sa.Column(
            'position',
            sa.Integer()
        ),
        sa.ForeignKeyConstraint(
            ['hearing_id'],
            ['hearing.id'],
            ondelete='CASCADE'
        ),
        sa.ForeignKeyConstraint(
            ['hearing_section_id'],
            ['hearing_section.id'],
            ondelete='CASCADE'
        ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        op.f('ix_image_hearing_id'),
        'image',
        ['hearing_id'],
        unique=False
    )
    op.create_index(
        op.f('ix_image_hearing_section_id'),
        'image',
        ['hearing_section_id'],
        unique=False
    )
    op.add_column(
        'comment',
        sa.Column(
            'image_id',
            sa.Integer(),
            nullable=True
        )
    )
    op.create_index(
        op.f('ix_comment_image_id'),
        'comment',
        ['image_id'],
        unique=False
    )
    op.add_column(
        'comment_version',
        sa.Column(
            'image_id',
            sa.Integer(),
        )
    )
    op.create_index(
        op.f('ix_comment_version_image_id'),
        'comment_version',
        ['image_id'],
        unique=False
    )
    op.add_column(
        'hearing',
        sa.Column(
            'main_image_id',
            sa.Integer(),
        )
    )
    op.add_column(
        'hearing_section',
        sa.Column(
            'main_image_id',
            sa.Integer(),
        )
    )
    op.add_column(
        'hearing_section_version',
        sa.Column(
            'main_image_id',
            sa.Integer(),
        )
    )
    op.add_column(
        'hearing_version',
        sa.Column(
            'main_image_id',
            sa.Integer(),
        )
    )

    op.drop_constraint('comment_check', 'comment')
    op.create_check_constraint(
        'comment_check',
        'comment',
        '(comment.comment_id IS NOT NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.hearing_section_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NOT NULL '
        'AND comment.hearing_section_id IS NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.hearing_section_id IS NOT NULL '
        'AND comment.image_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.hearing_section_id IS NULL '
        'AND comment.image_id IS NOT NULL) '
    )

    op.create_check_constraint(
        'image_check',
        'image',
        '(image.hearing_id IS NULL '
        'AND image.hearing_section_id IS NULL '
        'AND image.position IS NULL) '
        'OR '
        '(image.hearing_id IS NOT NULL '
        'AND image.hearing_section_id IS NULL '
        'AND image.position >= 0) '
        'OR '
        '(image.hearing_id IS NULL '
        'AND image.hearing_section_id IS NOT NULL '
        'AND image.position >= 0) '
    )

    op.create_foreign_key(
        'hearing_main_image_id_fkey',
        'hearing',
        'image',
        ['main_image_id'],
        ['id'],
        ondelete='SET NULL'
    )

    op.create_foreign_key(
        'hearing_section_main_image_id_fkey',
        'hearing_section',
        'image',
        ['main_image_id'],
        ['id'],
        ondelete='SET NULL'
    )


def downgrade():
    op.drop_constraint('hearing_section_main_image_id_fkey', 'hearing_section')
    op.drop_constraint('hearing_main_image_id_fkey', 'hearing')
    op.drop_constraint('comment_check', 'comment')
    op.create_check_constraint(
        'comment_check',
        'comment',
        '(comment.comment_id IS NOT NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.hearing_section_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NOT NULL '
        'AND comment.hearing_section_id IS NULL) '
        'OR '
        '(comment.comment_id IS NULL '
        'AND comment.hearing_id IS NULL '
        'AND comment.hearing_section_id IS NOT NULL)'
    )

    op.drop_column('hearing_version', 'main_image_id')
    op.drop_column('hearing_section_version', 'main_image_id')
    op.drop_column('hearing_section', 'main_image_id')
    op.drop_column('hearing', 'main_image_id')
    op.drop_index(
        op.f('ix_comment_version_image_id'), table_name='comment_version'
    )
    op.drop_column('comment_version', 'image_id')
    op.drop_index(op.f('ix_comment_image_id'), table_name='comment')
    op.drop_column('comment', 'image_id')
    op.drop_index(op.f('ix_image_hearing_section_id'), table_name='image')
    op.drop_index(op.f('ix_image_hearing_id'), table_name='image')
    op.drop_table('image')
