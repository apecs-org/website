#!/bin/bash
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

#!/bin/bash
set -eo pipefail
shopt -s nullglob

VENV_PYTHON="/home/apecsuser/apecs/.venv/bin/python"

# Migrate database
$VENV_PYTHON manage.py migrate

# If there is a command passed to the container, run it as-is
if [ $# -gt 0 ]; then
  exec "$@"
else
  # Default: launch Gunicorn
  if [ -x "/home/apecsuser/apecs/.venv/bin/gunicorn" ]; then
    exec /home/apecsuser/apecs/.venv/bin/gunicorn apecs.wsgi:application
  else
    echo "Gunicorn not found, nothing to run."
    exit 1
  fi
fi