using AutoMapper;
using Common;
using Moq;
using Persistence;
using Persistence<#package#>.Repositories;
using System;
using Xunit;

namespace UnitTests.<#package#>.Persistence<#package#>.Repositories
{
    public class <#name#>RepositoryTests : IDisposable
    {
        private readonly MockRepository _mockRepository;
        private readonly Mock<Lazy<WaWiContext>> _mockLazy;
        private readonly Mock<IMapper> _mockMapper;
        private readonly Mock<ICurrentUser> _mockCurrentUser;

        public  <#name#>RepositoryTests()
        {
            _mockRepository = new MockRepository(MockBehavior.Strict);
            _mockLazy = _mockRepository.Create<Lazy<WaWiContext>>();
            _mockMapper = _mockRepository.Create<IMapper>();
            _mockCurrentUser = _mockRepository.Create<ICurrentUser>();
        }

        public void Dispose()
        {
            _mockRepository.VerifyAll();
        }

        private <#name#>Repository Create<#name#>Repository()
        {
            return new <#name#>Repository(
                _mockLazy.Object,
                _mockMapper.Object,
                _mockCurrentUser.Object);
        }
    }
}