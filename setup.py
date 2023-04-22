# Copyright 2022 Harsimran Singh Maan
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup

setup(
        name='ptolemaios',
        version='0.0.1',
        description='My private package from private github repo',
        url='git@github.com:davies-w/ptolemaios-sdk-package.git',
        author='Winton Davies',
        author_email='wdavies@cs.stanford.edu',
        license='unlicense',
        install_requires=["numpy"],
        packages=['ptolemaios'],
        zip_safe=False
    )
